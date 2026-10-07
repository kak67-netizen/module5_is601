"""Tests for calculator observers."""

import pytest

from app.observers import Observer


def test_base_observer_update():
    """Base observer should require subclasses to implement update."""
    observer = Observer()

    with pytest.raises(NotImplementedError):
        observer.update("test_event")