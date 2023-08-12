# Copyright (c) 2022 IO-Aero. All rights reserved. Use of this
# source code is governed by the IO-Aero License, that can
# be found in the LICENSE.md file.
"""Global constants and variables."""
import logging.config

# Environment types.
ENVIRONMENT_TYPE_DEV = "dev"
ENVIRONMENT_TYPE_PROD = "prod"
ENVIRONMENT_TYPE_TEST = "test"

# Error messages.

# Default file encoding UTF-8.
FILE_ENCODING_DEFAULT = "utf-8"

# Informational messages.
INFO_00_001 = "INFO.00.001 The logger is configured and ready"

INFORMATION_NOT_YET_AVAILABLE = "n/a"

# Library version number.
IO_TEMPLATE_LIB_VERSION = "9.9.9"

# Logging constants.
LOGGER_END = "End"
LOGGER_NAME = "iotemplatelib"
LOGGER_START = "Start"

# Logger instance.
logger: logging.Logger = logging.getLogger(LOGGER_NAME)
