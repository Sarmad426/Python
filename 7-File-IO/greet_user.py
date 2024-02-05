"""
Python program for file input-output.
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


# Reading the name from the file


def read_file() -> str:
    """
    Reads the name from the file

    Takes no parameters

    returns the contents of the file
    """
    with open("practice.txt", "r", encoding="utf-8") as file:
        return file.read()


def greet_user(name: str) -> None:
    """
    Greets the user

    Parameters (1) name of type string \n
    name : str
    """
    print(f"Welcome, {name}")


def main():
    """
    Main function to execute all the functions.\n
    It doesn't take any parameters neither returns anything
    """
    name = get_input_name()
    validate_input(name)
    write_file(name)
    name = read_file()
    greet_user(name)


if __name__ == "__main__":
    main()
