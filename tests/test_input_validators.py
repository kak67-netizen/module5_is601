"""Tests for calculator input validation."""

import pytest

from app.input_validators import (
    validate_number,
    validate_operation,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        ("10", 10.0),
        ("5.5", 5.5),
        ("-3", -3.0),
        ("0", 0.0),
        (" 25 ", 25.0),
    ],
)
def test_validate_number(value, expected):
    """Valid numeric input should be converted to float."""
    assert validate_number(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "hello",
        "",
        "five",
    ],
)
def test_validate_number_invalid(value):
    """Invalid numeric input should raise ValueError."""
    with pytest.raises(
        ValueError,
        match="Invalid number",
    ):
        validate_number(value)


@pytest.mark.parametrize(
    "operation",
    [
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "root",
    ],
)
def test_validate_operation(operation):
    """Supported operations should be accepted."""
    assert validate_operation(operation) == operation


def test_validate_operation_normalizes_input():
    """Operation input should be stripped and lowercased."""
    assert validate_operation("  ADD  ") == "add"


def test_validate_operation_invalid():
    """Unsupported operations should raise ValueError."""
    with pytest.raises(
        ValueError,
        match="Invalid operation",
    ):
        validate_operation("banana")


def test_validate_operation_not_string():
    """Non-string operations should raise ValueError."""
    with pytest.raises(
        ValueError,
        match="Operation must be text",
    ):
        validate_operation(123)