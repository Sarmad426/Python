"""
Python code testing using `unittest`
"""

import unittest
from typing import Optional


def factorial(n: int) -> Optional[int]:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        Optional[int]: The factorial of the number, or None if the input is negative.
    """
    if n < 0:
        return None
    result: int = 1
    for i in range(2, n + 1):
        result *= i
    return result


class TestFactorial(unittest.TestCase):
    """
    Unit test class for testing the factorial function.
    """

    def test_factorial_positive(self) -> None:
        """
        Test factorial with positive integers.
        """
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_factorial_zero(self) -> None:
        """
        Test factorial with zero, which should return 1.
        """
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self) -> None:
        """
        Test factorial with a negative number, which should return None.
        """
        self.assertIsNone(factorial(-5))
        self.assertIsNone(factorial(-1))


if __name__ == "__main__":
    unittest.main()
