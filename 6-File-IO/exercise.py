"""
File IO exercise program
"""

import sys
from typing import Callable

get_input_name: Callable[[], str] = lambda: str(input("Name: ")).strip()


def validate_input(name: str) -> str:
    """
    Validates user input name.

    if input name exist, it returns the name, otherwise it exits the program with an error message
    """
    if not name:
        sys.exit("Name is required")

    return name


def write_file(name: str) -> None:
    """
    Writes a name into a file.

    Takes one parameter `name` and returns nothing
    """

    with open("practice.txt", "w", encoding="utf-8") as file:
        file.write(name)


def read_file() -> str:
    """
    Returns the contents of the file
    """
    with open("practice.txt", "r", encoding="utf-8") as file:
        return file.read()


def greet_user(name: str) -> None:
    """
    Greets the user

    Args:
        name (str)
    """
    print(f"Welcome, {name}")


def main():
    """
    Main function to execute all the functions.
    """
    name = get_input_name()
    validate_input(name)
    write_file(name)
    name = read_file()
    greet_user(name)


if __name__ == "__main__":
    main()
