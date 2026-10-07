"""Calculator facade connecting operations, history, and application state."""

from app.calculation import CalculationFactory
from app.calculator_config import CalculatorConfig
from app.calculator_memento import MementoManager
from app.history import History
from app.input_validators import validate_operation
from app.observers import AutoSaveObserver, LoggingObserver


class Calculator:
    """Facade for calculator operations and supporting subsystems."""

    def __init__(self) -> None:
        """Initialize calculator components."""
        self.config = CalculatorConfig()
        self.history = History()
        self.memento = MementoManager()
        self.observers = [LoggingObserver()]

        if self.config.auto_save:
            self.observers.append(
                AutoSaveObserver(
                    self.history,
                    str(self.config.history_path),
                )
            )

        self.history.load(str(self.config.history_path))

    def _notify(self, event: str, **kwargs) -> None:
        """Notify all registered observers."""
        for observer in self.observers:
            observer.update(event, **kwargs)

    def calculate(
        self,
        operation: str,
        a: float,
        b: float,
    ) -> float:
        """Perform a calculation and store it in history."""
        operation = validate_operation(operation)

        self.memento.save_state(self.history.data)

        calculation = CalculationFactory.create(
            operation,
            a,
            b,
        )

        result = calculation.perform()

        self.history.add(
            operation,
            a,
            b,
            result,
        )

        self._notify(
            "calculation_added",
            operation=operation,
            a=a,
            b=b,
            result=result,
        )

        return result

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.memento.save_state(self.history.data)
        self.history.clear()
        self._notify("history_cleared")

    def undo(self) -> None:
        """Restore the previous history state."""
        self.history.data = self.memento.undo(
            self.history.data
        )
        self._notify("history_changed")

    def redo(self) -> None:
        """Restore a previously undone history state."""
        self.history.data = self.memento.redo(
            self.history.data
        )
        self._notify("history_changed")

    def save_history(self) -> None:
        """Save history manually."""
        self.history.save(str(self.config.history_path))

    def load_history(self) -> None:
        """Load history manually."""
        self.history.load(str(self.config.history_path))