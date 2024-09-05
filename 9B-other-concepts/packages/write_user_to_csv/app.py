"""
Python package for writing user info in a csv file
"""

import csv
import re


def write_user_info(filename: str, user_info: list[str | int]) -> None:
    """Writes user info in a csv file

    Args:
        filename (_str_):
        user_info (_list_):
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Email"])
        writer.writerow(user_info)


def is_valid_name(name: str):
    """
    Validate name
    """
    # Only alphabetic characters
    return all(part.isalpha() for part in name.split())


def is_valid_email(email: str):
    """
    Validates email
    """
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(regex, email) is not None


def get_user_input():
    """Gets user input

    Returns:
        tuple: (name,email)
    """
    while True:
        name = input("Enter your name: ").strip()
        if not is_valid_name(name):
            print(
                "Invalid name. Please enter a valid name containing only English characters."
            )
            continue

        email = input("Enter your email: ").strip()
        if not is_valid_email(email):
            print("Invalid email. Please enter a valid email address.")
            continue

        return name, email
