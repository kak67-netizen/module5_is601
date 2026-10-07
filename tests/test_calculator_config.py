"""Tests for calculator configuration management."""

import pytest

from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError


def test_default_configuration(monkeypatch):
    """Default configuration values should be available."""
    monkeypatch.delenv("CALCULATOR_HISTORY_FILE", raising=False)
    monkeypatch.delenv("CALCULATOR_AUTO_SAVE", raising=False)

    config = CalculatorConfig()

    assert config.history_file == "data/history.csv"
    assert config.auto_save is True


@pytest.mark.parametrize(
    "value,expected",
    [
        ("true", True),
        ("TRUE", True),
        ("1", True),
        ("yes", True),
        ("false", False),
        ("0", False),
        ("no", False),
    ],
)
def test_auto_save_values(monkeypatch, value, expected):
    """Auto-save environment values should be interpreted correctly."""
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", value)

    config = CalculatorConfig()

    assert config.auto_save is expected


def test_custom_history_file(monkeypatch):
    """A custom history path should be loaded."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        "custom/calculations.csv",
    )

    config = CalculatorConfig()

    assert config.history_file == "custom/calculations.csv"
    assert str(config.history_path) == "custom/calculations.csv"


def test_empty_history_file(monkeypatch):
    """An empty history path should raise a configuration error."""
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", " ")

    with pytest.raises(
        ConfigurationError,
        match="CALCULATOR_HISTORY_FILE cannot be empty",
    ):
        CalculatorConfig()