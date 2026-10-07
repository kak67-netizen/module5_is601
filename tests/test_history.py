"""Tests for pandas-based calculation history."""

from unittest.mock import patch

import pandas as pd
import pytest

from app.exceptions import HistoryError
from app.history import History


def test_history_starts_empty():
    """New history should contain no calculations."""
    history = History()

    assert len(history) == 0
    assert history.data.empty


def test_add_history():
    """A calculation should be added to history."""
    history = History()

    history.add("add", 5, 3, 8)

    assert len(history) == 1
    assert history.data.iloc[0]["operation"] == "add"
    assert history.data.iloc[0]["result"] == 8


def test_multiple_history_entries():
    """History should store multiple calculations."""
    history = History()

    history.add("add", 5, 3, 8)
    history.add("multiply", 4, 5, 20)

    assert len(history) == 2


def test_clear_history():
    """Clearing history should remove all calculations."""
    history = History()

    history.add("add", 5, 3, 8)
    history.clear()

    assert len(history) == 0
    assert history.data.empty


def test_save_history(tmp_path):
    """History should be saved to a CSV file."""
    history = History()
    history.add("power", 2, 3, 8)

    filename = tmp_path / "history.csv"
    history.save(str(filename))

    assert filename.exists()

    saved_data = pd.read_csv(filename)

    assert len(saved_data) == 1
    assert saved_data.iloc[0]["operation"] == "power"
    assert saved_data.iloc[0]["result"] == 8


def test_load_history(tmp_path):
    """Existing CSV history should be loaded."""
    filename = tmp_path / "history.csv"

    pd.DataFrame(
        [
            {
                "operation": "multiply",
                "a": 6,
                "b": 7,
                "result": 42,
            }
        ]
    ).to_csv(filename, index=False)

    history = History()
    history.load(str(filename))

    assert len(history) == 1
    assert history.data.iloc[0]["operation"] == "multiply"
    assert history.data.iloc[0]["result"] == 42


def test_load_missing_file(tmp_path):
    """A missing history file should produce empty history."""
    history = History()

    filename = tmp_path / "does_not_exist.csv"
    history.load(str(filename))

    assert history.data.empty
    assert list(history.data.columns) == History.COLUMNS


def test_save_history_error():
    """Saving should raise HistoryError when the CSV cannot be written."""
    history = History()

    with patch.object(
        pd.DataFrame,
        "to_csv",
        side_effect=OSError("Save failed"),
    ):
        with pytest.raises(
            HistoryError,
            match="Unable to save history",
        ):
            history.save("data/history.csv")


def test_load_history_error(tmp_path):
    """Loading should raise HistoryError when the CSV cannot be read."""
    filename = tmp_path / "history.csv"
    filename.touch()

    with patch(
        "app.history.pd.read_csv",
        side_effect=OSError("Load failed"),
    ):
        with pytest.raises(
            HistoryError,
            match="Unable to load history",
        ):
            History().load(str(filename))