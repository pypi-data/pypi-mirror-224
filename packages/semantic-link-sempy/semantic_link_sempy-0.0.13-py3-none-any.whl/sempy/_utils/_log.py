import logging
import functools
import inspect
import pandas as pd
import json
import re
import sys
import time

from collections import Counter
from pathlib import Path
from typing import Dict, List
from sempy._version import get_versions

SEMPY_LOGGER_NAME = "SemPy"
MDS_LOG_TABLE = "SynapseMLLogs"
REDACTED = "'REDACTED'"

notebook_workspace_id = "local"
scrubber_regex = re.compile(r"'[^']*'")   # module global to avoid expensive recompilation
mds_fields: dict = {}


def _get_type_name(obj):
    t = type(obj)
    return t.__module__ + "." + t.__name__


def _scrub(msg):
    global scrubber_regex
    return scrubber_regex.sub(REDACTED, msg)


def _initialize_log(on_fabric: bool, env: str, notebook_workspace_id: str):
    global mds_fields, scrubber_regex

    mds_fields = {
        "mds_ComponentName": "SemPy",
        "mds_TelemetryApplicationInfo": {
            "ApplicationName": "SemPy",
            "ApplicationType": "python",
            "ApplicationVersion": get_versions()['version']
        },
        "mds_Workspace": notebook_workspace_id
    }

    if on_fabric:
        from synapse.ml.pymds.handler import SynapseHandler
        from synapse.ml.pymds.scrubbers.scrubber import IScrub

        # Use the pymds decorator after it's aligned with the one we have here
        # from synapse.ml.pymds.synapse_logger import DecoratorJSONFormatter

        class QuotedStringScrubber(IScrub):

            def scrub(self, msg: str) -> str:
                return _scrub(msg)

        scrubbers: List[IScrub] = [QuotedStringScrubber()] if env == "prod" else []
        logger = logging.getLogger(SEMPY_LOGGER_NAME)
        logger.setLevel(logging.DEBUG)
        handler = SynapseHandler(MDS_LOG_TABLE, scrubbers=scrubbers)
        handler.setFormatter(DecoratorJSONFormatter())
        logger.addHandler(handler)
        logger.propagate = False


def _sempy_extract_mds() -> Dict:
    global mds_fields
    return mds_fields


def _sempy_extract_message(result, arg_dict) -> Dict:
    d: dict = {}

    for arg, value in arg_dict.items():
        if isinstance(value, str):
            # Long strings and string that contain quotes should not be logged.
            # Quotes can interfere with redaction and JSON formatting.
            if len(value) > 40 or "'" in value or '"' in value:
                d[arg] = REDACTED
            else:
                d[arg] = f"'{value}'"
        elif isinstance(value, (int, float)):  # includes bool, which is an int
            d[arg] = value
        elif isinstance(value, pd.DataFrame):
            d[f"{arg}.type"] = _get_type_name(value)
            d[f"{arg}.shape"] = value.shape

    # Functions that do not return anything have the result of "None",
    # which will fail the tests on hasattr(). The result will thus
    # not appear in the dictionary and the message:
    if hasattr(result, 'shape'):
        d['result.shape'] = result.shape
    elif hasattr(result, '__len__'):
        d['result.len'] = len(result)

    return d


def _tables_extract_message(result, arg_dict) -> Dict:
    d = _sempy_extract_message(result, arg_dict)
    tables = arg_dict.get('tables')
    if isinstance(tables, dict):
        element_types = [_get_type_name(o) for o in tables.values()]
    elif isinstance(tables, list):
        element_types = [_get_type_name(o) for o in tables]
    else:
        element_types = _get_type_name(tables)
    d['tables'] = Counter(element_types)
    return d


def _retry_extract(result, arg_dict) -> Dict:
    d = _sempy_extract_message(result, arg_dict)
    d['status'] = arg_dict['self'].status
    d['total'] = arg_dict['self'].total
    return d


# ---------------- Begin code originating from Synapse-Utils (synapse_logger.py) ----------------------
# This version of the decorator avoids duplication of file_name, lineno, levelname, Throwable that is the
# feature of the current pymds version. As a result Message column is more compact and readable.

class DecoratorJSONFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord):
        if isinstance(record.args, dict):
            if 'func_name_override' in record.args:
                record.funcName = record.args['func_name_override']
            if 'file_name_override' in record.args:
                record.filename = record.args['file_name_override']
            if 'path_name_override' in record.args:
                record.pathname = record.args['path_name_override']
            if 'lineno_override' in record.args:
                record.lineno = record.args['lineno_override']
            if 'module_override' in record.args:
                record.module = record.args['module_override']

        return json.dumps(record.msg)


def _sempy_log(extract_message_fn):
    """
    Generate a decorator that invokes the logging method based on the execution environment.

    Parameters
    ----------
    extract_message_fn : callable
       Receive invocation args/kwargs and returns a dict to be added to the log message dictionary.

    Returns
    -------
    decorator
        Decorator that invokes the logging method based on the execution environment.
    """
    return mds_log(
        extract_message_fn=extract_message_fn,
        extract_mds_fn=_sempy_extract_mds,
        logger=logging.getLogger(SEMPY_LOGGER_NAME))


# ---------------- Begin code originating from Synapse-Utils (decorator.py) ----------------------

def mds_log(extract_message_fn, extract_mds_fn, logger):

    # logger = get_mds_json_logger("decorator") if logger is None else logger

    def get_wrapper(func):

        path_name_override = sys._getframe().f_back.f_code.co_filename
        file_name_override = Path(path_name_override).name
        lineno_override = sys._getframe().f_back.f_lineno

        @functools.wraps(func)
        def log_decorator_wrapper(*args, **kwargs):

            extra = {
                "log_kusto": True,
                "func_name_override": func.__name__,
                "module_override": func.__module__,
                "file_name_override": file_name_override,
                "path_name_override": path_name_override,
                "lineno_override": lineno_override
            }

            message = {"func": f"{func.__module__}.{func.__name__}"}

            try:
                if extract_mds_fn is not None:
                    extra.update(extract_mds_fn())

                s = inspect.signature(func)
                arg_dict = s.bind(*args, **kwargs).arguments

            except Exception:
                logger.error(message, extra, exc_info=True)
                raise

            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)

                # The invocation for extract_message_fn moves after the function
                # so it can access the state after the method call
                if extract_message_fn:
                    message.update(extract_message_fn(result, arg_dict))

                message["total_seconds"] = _round_significant(time.perf_counter() - start_time, 3)
                logger.info(message, extra)
            except Exception:
                # extract_message_fn itself could be the cause of the exception, which we have to catch
                # if we want to get a chance to log the original exception details
                try:
                    if extract_message_fn:
                        message.update(extract_message_fn(None, arg_dict))
                except Exception:
                    pass
                message["total_seconds"] = _round_significant(time.perf_counter() - start_time, 3)
                logger.error(message, extra, exc_info=True)
                raise
            return result

        return log_decorator_wrapper

    return get_wrapper


def _round_significant(num, digits):
    from math import log10, floor
    return round(num, digits-int(floor(log10(abs(num))))-1)

# ----------- End code originating from Synapse-Utils  ----------------------


log = _sempy_log(_sempy_extract_message)
log_retry = _sempy_log(_retry_extract)
log_tables = _sempy_log(_tables_extract_message)
