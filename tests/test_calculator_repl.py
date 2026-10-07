"""Tests for the calculator REPL."""

from unittest.mock import patch

import pytest

from app.calculator_repl import run_repl


def run_with_inputs(inputs):
    """Run the REPL using simulated user input."""
    with patch("builtins.input", side_effect=inputs):
        run_repl()


def test_exit(capsys, tmp_path, monkeypatch):
    """Exit command should close the calculator."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(["exit"])

    output = capsys.readouterr().out
    assert "Goodbye!" in output


def test_help(capsys, tmp_path, monkeypatch):
    """Help command should display available commands."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(["help", "exit"])

    output = capsys.readouterr().out
    assert "Available operations:" in output
    assert "undo" in output
    assert "redo" in output


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", "5", "3", "Result: 8.0"),
        ("subtract", "10", "4", "Result: 6.0"),
        ("multiply", "6", "7", "Result: 42.0"),
        ("divide", "10", "2", "Result: 5.0"),
        ("power", "2", "3", "Result: 8.0"),
        ("root", "25", "2", "Result: 5.0"),
    ],
)
def test_repl_calculations(
    capsys,
    tmp_path,
    monkeypatch,
    operation,
    a,
    b,
    expected,
):
    """REPL should perform supported calculations."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs([operation, a, b, "exit"])

    output = capsys.readouterr().out
    assert expected in output


def test_invalid_number(capsys, tmp_path, monkeypatch):
    """Invalid numeric input should be handled gracefully."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(["add", "hello", "exit"])

    output = capsys.readouterr().out
    assert "Error: Invalid number" in output


def test_division_by_zero(capsys, tmp_path, monkeypatch):
    """Division by zero should be handled gracefully."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(["divide", "10", "0", "exit"])

    output = capsys.readouterr().out
    assert "Error: Cannot divide by zero." in output


def test_history_clear_undo_redo(capsys, tmp_path, monkeypatch):
    """History and state commands should work through the REPL."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(
        [
            "add", "2", "3",
            "history",
            "clear",
            "undo",
            "redo",
            "exit",
        ]
    )

    output = capsys.readouterr().out

    assert "add" in output
    assert "History cleared." in output
    assert "Undo complete." in output
    assert "Redo complete." in output


def test_empty_history(capsys, tmp_path, monkeypatch):
    """Empty history should display a helpful message."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(["history", "exit"])

    output = capsys.readouterr().out
    assert "History is empty." in output


def test_save_and_load(capsys, tmp_path, monkeypatch):
    """Save and load commands should work."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    run_with_inputs(
        [
            "add", "2", "3",
            "save",
            "load",
            "exit",
        ]
    )

    output = capsys.readouterr().out

    assert "History saved." in output
    assert "History loaded." in output


def test_keyboard_interrupt(capsys, tmp_path, monkeypatch):
    """Keyboard interruption should exit gracefully."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history.csv"),
    )

    with patch(
        "builtins.input",
        side_effect=KeyboardInterrupt,
    ):
        run_repl()

    output = capsys.readouterr().out
    assert "Goodbye!" in output