"""Tests for the calculator Memento pattern."""

import pandas as pd

from app.calculator_memento import CalculatorMemento, MementoManager


def make_state(results):
    """Create a simple DataFrame state for testing."""
    return pd.DataFrame({"result": results})


def test_memento_stores_state():
    """A memento should preserve a calculator state."""
    original = make_state([5, 10])
    memento = CalculatorMemento(original)

    restored = memento.get_state()

    pd.testing.assert_frame_equal(restored, original)


def test_memento_returns_copy():
    """Changing a restored state should not alter the saved state."""
    original = make_state([5])
    memento = CalculatorMemento(original)

    restored = memento.get_state()
    restored.loc[0, "result"] = 99

    assert memento.get_state().loc[0, "result"] == 5


def test_undo():
    """Undo should restore the previous state."""
    manager = MementoManager()

    old_state = make_state([5])
    new_state = make_state([5, 10])

    manager.save_state(old_state)

    restored = manager.undo(new_state)

    pd.testing.assert_frame_equal(restored, old_state)


def test_redo():
    """Redo should restore the state that was undone."""
    manager = MementoManager()

    old_state = make_state([5])
    new_state = make_state([5, 10])

    manager.save_state(old_state)

    undone = manager.undo(new_state)
    restored = manager.redo(undone)

    pd.testing.assert_frame_equal(restored, new_state)


def test_undo_with_empty_stack():
    """Undo with no saved states should keep current state."""
    manager = MementoManager()
    current = make_state([5])

    restored = manager.undo(current)

    pd.testing.assert_frame_equal(restored, current)


def test_redo_with_empty_stack():
    """Redo with no saved states should keep current state."""
    manager = MementoManager()
    current = make_state([5])

    restored = manager.redo(current)

    pd.testing.assert_frame_equal(restored, current)


def test_new_state_clears_redo_stack():
    """Saving a new state after undo should clear redo history."""
    manager = MementoManager()

    first = make_state([5])
    second = make_state([5, 10])

    manager.save_state(first)
    manager.undo(second)

    new_state = make_state([5, 20])
    manager.save_state(first)

    restored = manager.redo(new_state)

    pd.testing.assert_frame_equal(restored, new_state)