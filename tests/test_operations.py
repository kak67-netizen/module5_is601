import pytest

from app.operations import (
    Add,
    Divide,
    Multiply,
    Operation,
    Power,
    Root,
    Subtract,
)
@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Add(), 5, 3, 8),
        (Add(), -5, 3, -2),
        (Subtract(), 10, 4, 6),
        (Subtract(), 4, 10, -6),
        (Multiply(), 6, 7, 42),
        (Multiply(), -2, 5, -10),
        (Divide(), 10, 2, 5),
        (Power(), 2, 3, 8),
        (Power(), 5, 0, 1),
        (Root(), 9, 2, 3),
        (Root(), 27, 3, 3),
    ],
)
def test_operations(operation, a, b, expected):
    """Test arithmetic operations with multiple inputs."""
    assert operation.execute(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    """Division by zero should raise an error."""
    with pytest.raises(
        ZeroDivisionError,
        match="Cannot divide by zero",
    ):
        Divide().execute(10, 0)


def test_zero_degree_root():
    """A root degree of zero should raise an error."""
    with pytest.raises(
        ValueError,
        match="Root degree cannot be zero",
    ):
        Root().execute(9, 0)


def test_even_root_of_negative_number():
    """An even root of a negative number should raise an error."""
    with pytest.raises(
        ValueError,
        match="Cannot calculate an even root",
    ):
        Root().execute(-16, 2)


def test_odd_root_of_negative_number():
    """Odd roots of negative numbers should work."""
    assert Root().execute(-27, 3) == pytest.approx(-3)

def test_base_operation_execute():
    """Cover the abstract base operation implementation."""

    class TestOperation(Operation):
        def execute(self, a, b):
            return super().execute(a, b)

    with pytest.raises(NotImplementedError):
        TestOperation().execute(1, 2)