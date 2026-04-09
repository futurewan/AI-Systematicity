"""Validation helpers."""


def is_positive_int(value: int) -> bool:
    """Return True only when value is int and > 0."""
    return isinstance(value, int) and value > 0
