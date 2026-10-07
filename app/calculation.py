"""Calculation model and factory for the calculator."""

from app.operations import (
    Add,
    Divide,
    Multiply,
    Operation,
    Power,
    Root,
    Subtract,
)


class Calculation:
    """Represent a completed calculation."""

    def __init__(self, a: float, b: float, operation: Operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> float:
        """Perform the stored operation."""
        return self.operation.execute(self.a, self.b)

    def __str__(self) -> str:
        """Return a readable description of the calculation."""
        result = self.perform()
        return (
            f"{self.a} {self.operation.__class__.__name__} "
            f"{self.b} = {result}"
        )


class CalculationFactory:
    """Create Calculation objects based on an operation name."""

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
    }

    @classmethod
    def create(cls, operation_name: str, a: float, b: float) -> Calculation:
        """Create a calculation using the requested operation."""
        operation_name = operation_name.lower()

        if operation_name not in cls.operations:
            raise ValueError(f"Unknown operation: {operation_name}")

        operation = cls.operations[operation_name]()
        return Calculation(a, b, operation)