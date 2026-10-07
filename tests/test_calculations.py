"""Tests for Calculation and CalculationFactory."""

import pytest

from app.calculation import Calculation, CalculationFactory
from app.operations import Add


def test_calculation_perform():
    """Test that a Calculation performs its operation."""
    calculation = Calculation(5, 3, Add())

    assert calculation.perform() == 8


def test_calculation_string():
    """Test the readable calculation representation."""
    calculation = Calculation(5, 3, Add())

    assert str(calculation) == "5 Add 3 = 8"


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 10, 5, 15),
        ("subtract", 10, 5, 5),
        ("multiply", 10, 5, 50),
        ("divide", 10, 5, 2),
        ("power", 2, 3, 8),
        ("root", 25, 2, 5),
    ],
)
def test_factory_operations(operation, a, b, expected):
    """Test that the factory creates each operation correctly."""
    calculation = CalculationFactory.create(
        operation,
        a,
        b,
    )

    assert calculation.perform() == pytest.approx(expected)


def test_factory_is_case_insensitive():
    """Operation names should not be case sensitive."""
    calculation = CalculationFactory.create(
        "ADD",
        4,
        6,
    )

    assert calculation.perform() == 10


def test_factory_invalid_operation():
    """Unknown operations should raise an error."""
    with pytest.raises(
        ValueError,
        match="Unknown operation",
    ):
        CalculationFactory.create(
            "banana",
            1,
            2,
        )