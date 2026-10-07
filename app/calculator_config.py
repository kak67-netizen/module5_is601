"""Configuration management for the calculator application."""

import os
from pathlib import Path

from dotenv import load_dotenv

from app.exceptions import ConfigurationError


class CalculatorConfig:
    """Load and validate calculator configuration."""

    def __init__(self) -> None:
        """Load configuration values from environment variables."""
        load_dotenv()

        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE",
            "data/history.csv",
        )

        self.auto_save = os.getenv(
            "CALCULATOR_AUTO_SAVE",
            "true",
        ).lower() in {"true", "1", "yes"}

        self.validate()

    def validate(self) -> None:
        """Validate configuration settings."""
        if not self.history_file.strip():
            raise ConfigurationError(
                "CALCULATOR_HISTORY_FILE cannot be empty."
            )

    @property
    def history_path(self) -> Path:
        """Return the configured history file as a Path."""
        return Path(self.history_file)