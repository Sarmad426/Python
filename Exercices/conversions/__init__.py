"""
Python custom helper functions
"""


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
