import logging
from typing import Callable


logging.basicConfig(level=logging.DEBUG)
pybitesLogger = logging.getLogger("pybites_logger")


DEBUG = pybitesLogger.debug
INFO = pybitesLogger.info
WARNING = pybitesLogger.warning
ERROR = pybitesLogger.error
CRITICAL = pybitesLogger.critical


def log_it(level: Callable, msg: str) -> None:
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
