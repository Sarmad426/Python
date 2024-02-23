"""
Python program converts binary input to decimal
"""

import sys
from helper_method import validate_binary


def binary_to_octal(binary: str) -> str:
    """
    Converts binary input to octal

    Parameters:
    - `binary` (str) : binary to convert

    Returns:
    - str : octal output
    """
    while len(binary) % 3 != 0:
        binary = "0" + binary

    octal = ""
    for i in range(0, len(binary), 3):
        chunk = binary[i : i + 3]
        octal += str(int(chunk, 2))
    return octal


BINARY_INPUT = input("Enter binary number: ")

if not validate_binary(BINARY_INPUT):
    sys.exit("Invalid binary value! ")
else:
    print("Octal Output: ", binary_to_octal(BINARY_INPUT))
