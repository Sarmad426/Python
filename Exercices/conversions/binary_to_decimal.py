"""
Python program converts binary input to decimal
"""

import re
import sys


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
    count = len(binary) - 1
    for digit in binary:
        mul = pow(2, power) * int(binary[count])
        power += 1
        total += mul
        count -= 1
    decimal = str(total)
    return str(decimal)


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
