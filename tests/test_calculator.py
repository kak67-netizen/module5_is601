"""Tests for the Calculator facade."""

import pandas as pd
import pytest

from app.calculator import Calculator


@pytest.fixture
def calculator(tmp_path, monkeypatch):
    """Create a calculator using a temporary history file."""
    history_file = tmp_path / "history.csv"

    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(history_file),
    )
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "true")

    return Calculator()


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
        ("multiply", 6, 7, 42),
        ("divide", 10, 2, 5),
        ("power", 2, 3, 8),
        ("root", 25, 2, 5),
    ],
)
def test_calculate(calculator, operation, a, b, expected):
    """Calculator should perform all supported operations."""
    result = calculator.calculate(operation, a, b)

    assert result == pytest.approx(expected)


def test_calculation_added_to_history(calculator):
    """Completed calculations should be stored in history."""
    calculator.calculate("add", 2, 3)

    assert len(calculator.history) == 1
    assert calculator.history.data.iloc[0]["result"] == 5


def test_auto_save(calculator):
    """Calculation history should be automatically saved."""
    calculator.calculate("multiply", 4, 5)

    assert calculator.config.history_path.exists()


def test_clear_history(calculator):
    """Clear should remove calculator history."""
    calculator.calculate("add", 1, 2)
    calculator.clear_history()

    assert calculator.history.data.empty


def test_undo(calculator):
    """Undo should restore the previous history state."""
    calculator.calculate("add", 1, 2)
    calculator.calculate("multiply", 3, 4)

    calculator.undo()

    assert len(calculator.history) == 1


def test_redo(calculator):
    """Redo should restore an undone state."""
    calculator.calculate("add", 1, 2)
    calculator.calculate("multiply", 3, 4)

    calculator.undo()
    calculator.redo()

    assert len(calculator.history) == 2


def test_manual_save_and_load(calculator):
    """History should support manual saving and loading."""
    calculator.calculate("add", 10, 5)
    calculator.save_history()

    calculator.history.clear()
    assert calculator.history.data.empty

    calculator.load_history()

    assert len(calculator.history) == 1


def test_invalid_operation(calculator):
    """Invalid operations should raise ValueError."""
    with pytest.raises(ValueError):
        calculator.calculate("banana", 1, 2)


def test_loaded_history(calculator):
    """Calculator history should use a pandas DataFrame."""
    calculator.calculate("power", 2, 4)

    assert isinstance(calculator.history.data, pd.DataFrame)