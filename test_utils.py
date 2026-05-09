"""Unit tests for date validation utilities in utils.py."""

import unittest
from datetime import date

from utils import validate_date, parse_date, format_date, get_current_date


class TestValidateDate(unittest.TestCase):
    """Tests for validate_date()."""

    # --- Valid dates ---
    def test_normal_date(self) -> None:
        self.assertTrue(validate_date("15-08-2025"))

    def test_first_day_of_year(self) -> None:
        self.assertTrue(validate_date("01-01-2025"))

    def test_last_day_of_year(self) -> None:
        self.assertTrue(validate_date("31-12-2025"))

    def test_leap_year_feb_29(self) -> None:
        self.assertTrue(validate_date("29-02-2024"))

    def test_single_digit_day_and_month(self) -> None:
        """DD-MM-YYYY requires zero-padded digits."""
        self.assertTrue(validate_date("01-01-2025"))

    # --- Invalid dates ---
    def test_non_leap_year_feb_29(self) -> None:
        self.assertFalse(validate_date("29-02-2023"))

    def test_invalid_month_20(self) -> None:
        """Catches the real bug in data.txt (20-20-2020)."""
        self.assertFalse(validate_date("20-20-2020"))

    def test_invalid_month_13(self) -> None:
        self.assertFalse(validate_date("01-13-2025"))

    def test_day_zero(self) -> None:
        self.assertFalse(validate_date("00-01-2025"))

    def test_day_32(self) -> None:
        self.assertFalse(validate_date("32-01-2025"))

    def test_empty_string(self) -> None:
        self.assertFalse(validate_date(""))

    def test_random_text(self) -> None:
        self.assertFalse(validate_date("not-a-date"))

    def test_wrong_separator(self) -> None:
        self.assertFalse(validate_date("15/08/2025"))

    def test_yyyy_mm_dd_format(self) -> None:
        """Reject ISO format — we only accept DD-MM-YYYY."""
        self.assertFalse(validate_date("2025-08-15"))

    def test_none_input(self) -> None:
        self.assertFalse(validate_date(None))  # type: ignore[arg-type]

    def test_numeric_input(self) -> None:
        self.assertFalse(validate_date(12345))  # type: ignore[arg-type]


class TestParseDate(unittest.TestCase):
    """Tests for parse_date()."""

    def test_valid_date_returns_date_object(self) -> None:
        result = parse_date("01-01-2025")
        self.assertEqual(result, date(2025, 1, 1))

    def test_leap_year(self) -> None:
        result = parse_date("29-02-2024")
        self.assertEqual(result, date(2024, 2, 29))

    def test_invalid_date_returns_none(self) -> None:
        self.assertIsNone(parse_date("29-02-2023"))

    def test_empty_string_returns_none(self) -> None:
        self.assertIsNone(parse_date(""))

    def test_none_input_returns_none(self) -> None:
        self.assertIsNone(parse_date(None))  # type: ignore[arg-type]


class TestFormatDate(unittest.TestCase):
    """Tests for format_date()."""

    def test_formats_correctly(self) -> None:
        self.assertEqual(format_date(date(2026, 5, 8)), "08-05-2026")

    def test_pads_single_digits(self) -> None:
        self.assertEqual(format_date(date(2025, 1, 1)), "01-01-2025")

    def test_roundtrip_with_parse(self) -> None:
        """parse_date → format_date should return the original string."""
        original = "15-08-2025"
        self.assertEqual(format_date(parse_date(original)), original)  # type: ignore[arg-type]


class TestGetCurrentDate(unittest.TestCase):
    """Tests for get_current_date()."""

    def test_returns_string(self) -> None:
        self.assertIsInstance(get_current_date(), str)

    def test_returned_string_is_valid(self) -> None:
        self.assertTrue(validate_date(get_current_date()))

    def test_matches_today(self) -> None:
        result = parse_date(get_current_date())
        self.assertEqual(result, date.today())


if __name__ == "__main__":
    unittest.main()
