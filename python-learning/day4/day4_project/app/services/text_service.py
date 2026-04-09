"""String utilities used by the demo app."""


def normalize_name(name: str) -> str:
    """Trim spaces and title-case a user name."""
    return name.strip().title()
