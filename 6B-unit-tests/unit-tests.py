"""
Python Unit Tests using Pytest
"""


def add_numbers(a: int, b: int) -> int:
    """
    Add a number
    """

    return a + b


def test_add_positive_numbers():
    """
    Test adding positive numbers
    """

    result = add_numbers(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """
    Test adding negative numbers
    """

    result = add_numbers(-2, -3)
    assert result == -5
