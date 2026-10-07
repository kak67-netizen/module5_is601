"""Calculation history management using pandas."""

from pathlib import Path

import pandas as pd

from app.exceptions import HistoryError


class History:
    """Manage calculator history using a pandas DataFrame."""

    COLUMNS = ["operation", "a", "b", "result"]

    def __init__(self):
        """Create an empty calculation history."""
        self.data = pd.DataFrame(columns=self.COLUMNS)

    def add(
        self,
        operation: str,
        a: float,
        b: float,
        result: float,
    ) -> None:
        """Add a calculation to the history."""
        new_row = pd.DataFrame(
            [
                {
                    "operation": operation,
                    "a": a,
                    "b": b,
                    "result": result,
                }
            ]
        )

        self.data = pd.concat(
            [self.data, new_row],
            ignore_index=True,
        )

    def clear(self) -> None:
        """Clear all calculation history."""
        self.data = pd.DataFrame(columns=self.COLUMNS)

    def save(self, filename: str) -> None:
        """Save calculation history to a CSV file."""
        try:
            path = Path(filename)
            path.parent.mkdir(parents=True, exist_ok=True)
            self.data.to_csv(path, index=False)
        except (OSError, PermissionError) as exc:
            raise HistoryError(
                f"Unable to save history: {filename}"
            ) from exc

    def load(self, filename: str) -> None:
        """Load calculation history from a CSV file."""
        path = Path(filename)

        if not path.exists():
            self.data = pd.DataFrame(columns=self.COLUMNS)
            return

        try:
            self.data = pd.read_csv(path)
        except (OSError, pd.errors.ParserError) as exc:
            raise HistoryError(
                f"Unable to load history: {filename}"
            ) from exc

    def __len__(self) -> int:
        """Return the number of calculations in history."""
        return len(self.data)