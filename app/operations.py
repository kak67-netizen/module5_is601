"""Arithmetic operation strategies for the calculator."""

from abc import ABC, abstractmethod


class Operation(ABC):
    """Base strategy for arithmetic operations."""

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Perform an arithmetic operation."""
        raise NotImplementedError


class Add(Operation):
    """Add two numbers."""

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    """Subtract the second number from the first."""

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    """Multiply two numbers."""

    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    """Divide the first number by the second."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class Power(Operation):
    """Raise the first number to the power of the second."""

    def execute(self, a: float, b: float) -> float:
        return a ** b


class Root(Operation):
    """Calculate the b-th root of a."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Root degree cannot be zero.")

        if a < 0 and b % 2 == 0:
            raise ValueError("Cannot calculate an even root of a negative number.")

        if a < 0:
            return -((-a) ** (1 / b))

        return a ** (1 / b)