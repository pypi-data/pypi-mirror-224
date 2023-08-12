# Copyright (c) 2022 IO-Aero. All rights reserved. Use of this
# source code is governed by the IO-Aero License, that can
# be found in the LICENSE.md file.
"""io_utils: coverage testing."""

from iotemplatelib import io_logger

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test case: initialise_logger() - Initialising the logging functionality.
# -----------------------------------------------------------------------------
def test_initialise_logger():
    """Test case: initialise_logger() - Initialising the logging functionality."""
    # pylint: disable=duplicate-code
    io_logger.initialise_logger()


# -----------------------------------------------------------------------------
# Test case: progress_msg() - Create a progress message.
# -----------------------------------------------------------------------------
def test_progress_msg():
    """Test case: progress_msg() - Create a progress message."""
    io_logger.initialise_logger()
    io_logger.io_log.info("Hello World! (from progress_msg())")


def test_changing_levels():
    """Test all the possible levels to make sure we can change to them all."""
    io_logger.initialise_logger()
    assert io_logger.set_logging_level(0) == 0
    assert io_logger.set_logging_level(1) == 0
    assert io_logger.set_logging_level(2) == 0
    assert io_logger.set_logging_level(3) == 0
    assert io_logger.set_logging_level(4) == 0
    assert io_logger.set_logging_level(5) == 0
    assert io_logger.set_logging_level(6) == -1


# # -----------------------------------------------------------------------------
# # Test case: progress_msg_core() - Create a progress message.
# # -----------------------------------------------------------------------------
# def test_progress_msg_core():
#     """Test case: progress_msg_core() - Create a progress message."""
#     io_utils.progress_msg_core(msg="Hello World! (from progress_msg_core())")
