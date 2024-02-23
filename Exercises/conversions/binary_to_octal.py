"""
Python program converts binary input to decimal
"""

import sys
from helper_method import (
    reverse_string,
    validate_binary,
    power_func,
)


def binary_to_octal(binary: str) -> str:
    """
    Converts binary input to octal

    Parameters:
    - `binary` (str) : binary to convert

    Returns:
    - str : octal output
    """
    octal = ""
    binary = reverse_string(binary)
    count = 0
    add = 0
    total = 0
    for i in range(len(binary)):
        count += 1
        add += int(binary[i]) * power_func(2, count - 1)  # 1,0,5,
        if count == 3:
            total = add
            print(count, add)
            count = 0
            add = 0
            octal += str(total)

    return reverse_string(octal)


BINARY_INPUT = input("Enter binary number: ")

if not validate_binary(BINARY_INPUT):
    sys.exit("Invalid binary value! ")
else:
    print("Octal Output: ", binary_to_octal(BINARY_INPUT))
