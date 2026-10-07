"""Memento pattern implementation for calculator history."""

from copy import deepcopy

import pandas as pd


class CalculatorMemento:
    """Store a snapshot of calculator history."""

    def __init__(self, state: pd.DataFrame):
        """Create a snapshot of the supplied history state."""
        self._state = deepcopy(state)

    def get_state(self) -> pd.DataFrame:
        """Return a copy of the saved state."""
        return deepcopy(self._state)


class MementoManager:
    """Manage undo and redo states for the calculator."""

    def __init__(self):
        """Initialize empty undo and redo stacks."""
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, state: pd.DataFrame) -> None:
        """Save the current state before it changes."""
        self._undo_stack.append(CalculatorMemento(state))
        self._redo_stack.clear()

    def undo(self, current_state: pd.DataFrame) -> pd.DataFrame:
        """Restore the previous state."""
        if not self._undo_stack:
            return current_state

        self._redo_stack.append(CalculatorMemento(current_state))
        memento = self._undo_stack.pop()
        return memento.get_state()

    def redo(self, current_state: pd.DataFrame) -> pd.DataFrame:
        """Restore a previously undone state."""
        if not self._redo_stack:
            return current_state

        self._undo_stack.append(CalculatorMemento(current_state))
        memento = self._redo_stack.pop()
        return memento.get_state()