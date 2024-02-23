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


if __name__ == "__main__":

    INPUT = input("Input string: ")

    print(reverse_string(INPUT))
