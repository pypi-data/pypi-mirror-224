"""Test the configuration main file."""
from iotemplatelib.io_settings import settings


def test_dynaconf_settings():
    """Test the dynaconf settings functionality."""
    assert settings.is_verbose is True
