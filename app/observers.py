"""Observer pattern implementations for calculator events."""

import logging

from app.history import History


class Observer:
    """Base observer interface."""

    def update(self, event: str, **kwargs) -> None:
        """React to a calculator event."""
        raise NotImplementedError


class LoggingObserver(Observer):
    """Log calculator events."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def update(self, event: str, **kwargs) -> None:
        """Log an event and its associated information."""
        self.logger.info(
            "Calculator event: %s | %s",
            event,
            kwargs,
        )


class AutoSaveObserver(Observer):
    """Automatically save history after calculation events."""

    def __init__(self, history: History, filename: str) -> None:
        self.history = history
        self.filename = filename

    def update(self, event: str, **kwargs) -> None:
        """Save history when it has been modified."""
        if event in {"calculation_added", "history_cleared"}:
            self.history.save(self.filename)