"""
Python custom helper functions
"""

import re


def reverse_string(string: str) -> str:
    """
    Reverses the string and returns it
    """
    reverse = ""
    index = len(string) - 1

    while index >= 0:
        reverse = reverse + string[index]
        index -= 1
    return reverse


def validate_binary(binary: str) -> bool:
    """
    Validates binary input via REGEX

    Parameter:
    `binary` (str) : binary value to validate

    Returns:
    bool : True if valid binary number
    """
    pattern = re.compile(r"^[01]+$")
    return bool(pattern.match(binary))


def power_func(num: int, power_digit: int) -> int:
    """
    Returns the power of the given number

    Parameters:
    - `num` (int) : number for power
    - `pow` (int) : power digit

    Returns the power of the given number
    """
    if power_digit == 0:
        return 1
    TEMP = num
    count = power_digit
    while count > 1:
        count -= 1
        num *= TEMP
    return num
