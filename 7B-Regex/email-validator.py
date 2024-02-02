"""
Email Validator Program in python using REGEX.
"""

import re


def validate_email(email: str) -> bool:
    """
    Validates an email address using regex.

    Parameters:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    return bool(pattern.fullmatch(email))


def main():
    """
    main function
    """
    user_email = input("Enter your email address: ")

    if validate_email(user_email):
        print("Valid email address.")
    else:
        print("Invalid email address. Please enter a valid email.")


if __name__ == "__main__":
    main()
