"""
Python practice programs for File Input-Output.
"""

import sys


def validate_input(name: str) -> str:
    """
    Validates user input name.
    if input exist it returns it,
    otherwise it exits the program
    """
    if not name:
        sys.exit("Name is required")

    return name


def write_file(name: str) -> None:
    """
    function for writing a name into a file.
    """

    with open("practice.txt", "w", encoding="utf-8") as file:
        file.write(name)


# Reading the name from the file
def read_file():
    """
    Reads the name from the file and greets the user
    """
    with open("practice.txt", "r", encoding="utf-8") as file:
        return file.read()


def greet_user(name: str) -> None:
    print(f"Welcome, {name}")


def main():
    """
    Main function to execute all the functions
    """
    name = str(input("Name: ")).strip()
    validate_input(name)
    write_file(name)
    name = read_file()
    greet_user(name)


if __name__ == "__main__":
    main()
