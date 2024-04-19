"""
Python program converts decimal input to binary
"""

from helper_method import reverse_string


def decimal_to_binary(decimal: int) -> str:
    """
    Converts decimal input to binary

    Parameters:
    - `binary` (int) : decimal to convert

    Returns:
    - str : binary output
    """
    binary = ""
    while decimal >= 1:
        temp = decimal % 2
        decimal = int(decimal / 2)
        binary = binary + str(temp)
    return reverse_string(binary)


DECIMAL_INPUT = int(input("Enter decimal number: "))


BINARY = decimal_to_binary(DECIMAL_INPUT)

print(f"Binary output: {BINARY}")
