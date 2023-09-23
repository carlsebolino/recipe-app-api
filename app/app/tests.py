"""
Sample tests

"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self) -> None:
        """Test adding numbers together"""
        res = calc.add(5, 10)
        self.assertEqual(res, 15)

    def test_subtract_numbers(self) -> None:
        """Test subtracting numbers."""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)
