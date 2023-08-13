import collections
import datetime
import json
import logging
from typing import (
    Any,
    Dict,
    Optional,
)

_STANDARD_ATTR = (
    "name",
    "msg",
    "args",
    "levelname",
    "levelno",
    "pathname",
    "filename",
    "module",
    "exc_info",
    "exc_text",
    "stack_info",
    "lineno",
    "funcName",
    "created",
    "msecs",
    "relativeCreated",
    "thread",
    "threadName",
    "processName",
    "process",
    "message",
    "asctime",
)

CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

_loggers = {}


def _extra_attributes(record: logging.LogRecord) -> Dict[str, Any]:
    """

    :param record: logging.LogRecord:

    """
    return {name: record.__dict__[name] for name in set(record.__dict__).difference(_STANDARD_ATTR)}


def _value(record: logging.LogRecord, field_name_or_value: Any) -> Any:
    """Retrieve value from record if possible. Otherwise use value.

    :param record: The record to extract a field named as in
        field_name_or_value.
    :type record: logging.LogRecord
    :param field_name_or_value: The field name to extract from record or
        the default value to use if not present.
    :type field_name_or_value: any
    :param record: logging.LogRecord:
    :param field_name_or_value: any
    """
    try:
        return getattr(record, field_name_or_value)
    except BaseException:
        return field_name_or_value


def _filter_empty(extra: Dict) -> Dict:
    """

    :param extra: Dict:

    """
    return {k: v for k, v in extra.items() if v}


def default_converter(obj: Any) -> str:
    """

    :param obj: Any:

    """
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    return str(obj)


class JSONFormatter(logging.Formatter):
    """"""

    def __init__(
        self,
        *args,
        fields: Dict[str, Any] = None,
        message_field_name: str = "message",
        exception_field_name: Optional[str] = "exception",
        indent: int = 4,
        verbose: bool = False,
        **kwargs,
    ):
        # Allow to provide any formatter setting (useful to provide a custom date format)
        super().__init__(*args, **kwargs)
        self.fields = fields or {}
        self.usesTime = lambda: "asctime" in self.fields.values()
        self.message_field_name = message_field_name
        self.exception_field_name = exception_field_name
        self.indent = indent
        self.verbose = verbose

    def format(self, record: logging.LogRecord):
        """

        :param record: logging.LogRecord

        """
        # Let python set every additional record field
        super().format(record)

        message = {field_name: _value(record, field_value) for field_name, field_value in self.fields.items()}
        if isinstance(record.msg, collections.abc.Mapping):
            message.update(record.msg)
        else:
            message[self.message_field_name] = super().formatMessage(record)

        message.update(_extra_attributes(record))

        if self.verbose:
            message["extra"] = _filter_empty(record.__dict__)

        if self.exception_field_name and record.exc_info:
            message[self.exception_field_name] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "stack": self.formatException(record.exc_info),
            }

        if len(message) == 1 and self.message_field_name in message:
            return super().formatMessage(record)

        return json.dumps(message, default=default_converter, indent=self.indent)

    def formatMessage(self, record: logging.LogRecord) -> str:
        """

        :param record: logging.LogRecord

        """
        # Speed up this step by doing nothing
        return ""


def get_logger(name: str, level: int = logging.INFO, verbose: bool = False) -> logging.Logger:
    """Returns a logger with a JSON formatter that supports structured logging.
    Can be called multiple times. It maintains a list of already initialized
    loggers, indexed by Name.

    :param name: Name of the Logger
    :type name: str
    :param level: Maximum level of the logs to print
    :type level: int
    :param verbose: (bool): If true add all supported fields
    :returns: logging.Logger
    :rtype: logging.Logger
    """
    global _loggers

    # Initialize the logger for a name only once
    if _loggers.get(name):
        return _loggers.get(name)

    logger = logging.getLogger(name)
    logger.propagate = False
    # logger.removeHandler(logging.getLogger().handlers[0])
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(
        JSONFormatter(
            fields={
                "timestamp": "asctime",
                "level": "levelname",
                "message": "msg",
                "class": "name",
                "module": "module",
                "filename": "filename",
                "line": "lineno",
            },
            verbose=verbose,
        )
    )
    logger.addHandler(handler)
    _loggers[name] = logger
    return logger
