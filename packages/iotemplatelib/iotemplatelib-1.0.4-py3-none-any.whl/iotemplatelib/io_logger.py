# Copyright (c) 2022 IO-Aero. All rights reserved. Use of this
# source code is governed by the IO-Aero License, that can
# be found in the LICENSE.md file.
"""Functions to setup and use the logger and others."""
import logging
import logging.config

from iotemplatelib import io_glob

# ------------------------------------------------------------------
# Global constants.
# ------------------------------------------------------------------
_LOGGER_CFG_FILE = "logging_cfg.yaml"
_LOGGER_FATAL_HEAD = "FATAL ERROR: program abort =====> "
_LOGGER_FATAL_TAIL = " <===== FATAL ERROR"
_LOGGER_PROGRESS_UPDATE = "Progress update "
LOGGER_END = "End"
LOGGER_NAME = "iotemplatelib"
LOGGER_START = "Start"

io_log: logging.Logger = logging.getLogger(LOGGER_NAME)


# -----------------------------------------------------------------------------
# Initialising the logging functionality.
# -----------------------------------------------------------------------------
def initialise_logger(log_level: int = 4) -> None:
    """Initialise the root logging functionality.Run this before you run
    io_glob.logger.info('msg') or anything like that.

    Args:
        log_level (int default 4): 0 for no messages, 1 for critical, 2 for error and above,
            3 for warning and above, 4 for info and above, 5 for all messages
    """
    form = logging.Formatter("%(asctime)s : %(levelname)-5.5s : %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(form)
    if not io_log.handlers:
        io_log.addHandler(console_handler)
        set_logging_level(level=log_level)
    io_log.info(
        "You are using IO-TEMPLATE-LIB version %s Copyright IO-Aero 2023",
        io_glob.IO_TEMPLATE_LIB_VERSION,
    )
    io_log.info("The logger is configured and ready use:")
    io_log.info("use io_log.(debug(),info(),warning(),error(), critcal())")


def set_logging_level(level: int) -> int:
    """Set the level of the logs that get written to screen.  the levels are
    debug, info, warning, error, critical in order from least to most prioirty.

    Args:
        level (int): 0 for no messages, 1 for critical, 2 for error and above,
            3 for warning and above, 4 for info and above, 5 for all messages

    Return:
        (int) 0 for no error, -1 for error
    """
    if level == 0:
        io_log.setLevel(51)
    elif level == 1:
        io_log.setLevel(logging.CRITICAL)
    elif level == 2:
        io_log.setLevel(logging.ERROR)
    elif level == 3:
        io_log.setLevel(logging.WARNING)
    elif level == 4:
        io_log.setLevel(logging.INFO)
    elif level == 5:
        io_log.setLevel(logging.DEBUG)
    else:
        io_log.warning("Logging level %d not understood and not set", level)
        return -1
    return 0
