"""
Python custom helper functions
"""


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


INPUT = input("Input string: ")

print(reverse_string(INPUT))
