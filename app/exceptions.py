"""Custom exceptions for the calculator application."""


class CalculatorError(Exception):
    """Base exception for calculator-related errors."""


class InvalidOperationError(CalculatorError):
    """Raised when an unsupported operation is requested."""


class CalculationError(CalculatorError):
    """Raised when a calculation cannot be completed."""


class ConfigurationError(CalculatorError):
    """Raised when application configuration is invalid."""


class HistoryError(CalculatorError):
    """Raised when calculation history cannot be saved or loaded."""