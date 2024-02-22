"""
Python program converts decimal input to binary
"""


def reverse_string(string: str) -> str:
    """
    Reverses the string and returns it
    """
    reverse = ""
    count = len(string) - 1

    for digit in string:
        reverse = reverse + string[count]
        count -= 1
    return reverse


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
