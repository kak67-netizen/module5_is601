"""Tests for custom calculator exceptions."""

import pytest

from app.exceptions import (
    CalculatorError,
    CalculationError,
    ConfigurationError,
    HistoryError,
    InvalidOperationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        InvalidOperationError,
        CalculationError,
        ConfigurationError,
        HistoryError,
    ],
)
def test_custom_exceptions_inherit_from_calculator_error(exception_class):
    """All custom calculator errors should inherit from CalculatorError."""
    assert issubclass(exception_class, CalculatorError)


@pytest.mark.parametrize(
    "exception_class",
    [
        CalculatorError,
        InvalidOperationError,
        CalculationError,
        ConfigurationError,
        HistoryError,
    ],
)
def test_exception_messages(exception_class):
    """Custom exceptions should preserve their messages."""
    error = exception_class("Test error")

    assert str(error) == "Test error"