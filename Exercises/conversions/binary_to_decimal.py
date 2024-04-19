"""
Python program converts binary input to decimal
"""

import sys
from helper_method import reverse_string, validate_binary


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


BINARY_INPUT = input("Enter binary number: ")

if not validate_binary(BINARY_INPUT):
    sys.exit("Invalid binary value! ")
else:
    print("Decimal Output: ", binary_to_decimal(BINARY_INPUT))
