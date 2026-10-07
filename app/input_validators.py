"""Input validation utilities for the calculator."""


VALID_OPERATIONS = {
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "root",
}


def validate_number(value: str) -> float:
    """Convert user input to a float or raise a helpful error."""
    try:
        return float(value)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid number: {value}") from exc


def validate_operation(operation: str) -> str:
    """Validate and normalize an operation name."""
    if not isinstance(operation, str):
        raise ValueError("Operation must be text.")

    operation = operation.strip().lower()

    if operation not in VALID_OPERATIONS:
        raise ValueError(f"Invalid operation: {operation}")

    return operation