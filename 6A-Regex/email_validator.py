"""
Email Validator Program in python using REGEX.
"""

import re


def validate_email(email: str) -> bool:
    """
    Validates an email address using regex.
    """

    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    return bool(pattern.fullmatch(email))


def main():
    """
    main function
    """
    user_email = input("Enter email: ")

    if validate_email(user_email):
        print("✅Valid email")
    else:
        print("⚠️Invalid email!")


if __name__ == "__main__":
    main()
