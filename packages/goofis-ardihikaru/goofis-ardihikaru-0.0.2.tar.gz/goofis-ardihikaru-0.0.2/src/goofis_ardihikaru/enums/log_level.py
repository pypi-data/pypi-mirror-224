import logging
from enum import Enum


class Loglevel(Enum):
    """ Log Level enums """

    FATAL = "FATAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    WARN = "WARN"
    INFO = "INFO"
    DEBUG = "DEBUG"


def to_level(level: str) -> int:
    """ Log Level enums """
    if level == Loglevel.FATAL.value:
        return logging.FATAL
    elif level == Loglevel.ERROR.value:
        return logging.ERROR
    elif level == Loglevel.WARNING.value:
        return logging.WARNING
    elif level == Loglevel.WARN.value:
        return logging.WARN
    elif level == Loglevel.INFO.value:
        return logging.INFO
    elif level == Loglevel.DEBUG.value:
        return logging.DEBUG
    else:
        return logging.INFO
