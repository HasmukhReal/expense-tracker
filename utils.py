"""Date validation utilities for the Expense Tracker.

All date functions use the DD-MM-YYYY format, which is the standard
format used throughout this project (see data/data.txt and main.py).

Functions:
    validate_date  — Check if a date string is valid.
    parse_date     — Convert a date string to a date object.
    format_date    — Convert a date object back to a string.
    get_current_date — Get today's date as a formatted string.
"""

from datetime import date, datetime

# The single source of truth for the date format used across the project.
DATE_FORMAT: str = "%d-%m-%Y"


def validate_date(date_str: str) -> bool:
    """Check whether *date_str* represents a valid date in DD-MM-YYYY format.

    Handles leap years correctly (delegated to ``datetime.strptime``).
    Returns ``False`` for any malformed or out-of-range input instead of
    raising an exception.

    Args:
        date_str: The date string to validate (e.g. "28-02-2024").

    Returns:
        True if the string is a valid DD-MM-YYYY date, False otherwise.

    Examples:
        >>> validate_date("15-08-2025")
        True
        >>> validate_date("29-02-2024")   # 2024 is a leap year
        True
        >>> validate_date("29-02-2023")   # 2023 is NOT a leap year
        False
        >>> validate_date("20-20-2020")   # month 20 is invalid
        False
        >>> validate_date("")
        False
    """
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except (ValueError, TypeError):
        return False


def parse_date(date_str: str) -> date | None:
    """Parse a DD-MM-YYYY string into a :class:`datetime.date` object.

    This is useful when you need to perform date arithmetic or comparisons
    (e.g. filtering expenses by date range).

    Args:
        date_str: The date string to parse (e.g. "01-01-2025").

    Returns:
        A ``date`` object on success, or ``None`` if parsing fails.

    Examples:
        >>> parse_date("01-01-2025")
        datetime.date(2025, 1, 1)
        >>> parse_date("invalid") is None
        True
    """
    try:
        return datetime.strptime(date_str, DATE_FORMAT).date()
    except (ValueError, TypeError):
        return None


def format_date(date_obj: date) -> str:
    """Format a :class:`datetime.date` object as a DD-MM-YYYY string.

    This is the inverse of :func:`parse_date`.

    Args:
        date_obj: The date object to format.

    Returns:
        A string in DD-MM-YYYY format (e.g. "08-05-2026").

    Raises:
        AttributeError: If *date_obj* is not a date/datetime instance.

    Examples:
        >>> from datetime import date
        >>> format_date(date(2026, 5, 8))
        '08-05-2026'
    """
    return date_obj.strftime(DATE_FORMAT)


def get_current_date() -> str:
    """Return today's date as a DD-MM-YYYY string.

    Useful as a default when the user doesn't supply a date.

    Returns:
        Today's date formatted as DD-MM-YYYY (e.g. "08-05-2026").

    Examples:
        >>> isinstance(get_current_date(), str)
        True
        >>> validate_date(get_current_date())
        True
    """
    return format_date(date.today())
