import logging.config

from iotemplatelib import io_glob as io_glob

LOGGER_END: str
LOGGER_NAME: str
LOGGER_START: str
io_log: logging.Logger

def initialise_logger(log_level: int = ...) -> None: ...
def set_logging_level(level: int) -> int: ...
