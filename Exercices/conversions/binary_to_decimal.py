"""
Python program converts binary input to decimal
"""

import re
import sys


def reverse_string(string: str) -> str:
    """
    Reverses the string and returns it
    """
    reverse = ""
    index = len(string) - 1

    for digit in string:
        reverse = reverse + string[index]
        index -= 1
    return reverse


def binary_to_decimal(binary: str) -> str:
    """
    Converts binary input to decimal

    Parameters:
    - `binary` (str) : binary to convert

    Returns:
    - str : decimal output
    """
    total = 0
    power = 0
    binary = reverse_string(binary)
    for digit in binary:
        mul = pow(2, power) * int(digit)
        power += 1
        total += mul
    decimal = str(total)
    return decimal


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


BINARY_INPUT = input("Enter binary number: ")

if not validate_binary(BINARY_INPUT):
    sys.exit("Invalid binary value! ")
else:
    print("Decimal Output: ", binary_to_decimal(BINARY_INPUT))
