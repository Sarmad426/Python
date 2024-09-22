"""
Password Strength Checker
"""

import re


def check_password_strength(password: str) -> int:
    """
    Checks the strength of the password based on the following criteria:

    1. Length >= 8
    2. Contains lowercase letters
    3. Contains uppercase letters
    4. Contains numbers
    5. Contains special characters (@#$%+=!)

    Args:
        password: The password to check
    """
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%+=!]", password):
        strength += 1

    return strength


def main():
    """
    Main function
    """
    password = input("Enter a password: ")
    strength = check_password_strength(password)

    if strength == 5:
        print("Password strength: Very Strong")
    elif strength == 4:
        print("Password strength: Strong")
    elif strength == 3:
        print("Password strength: Medium")
    elif strength == 2:
        print("Password strength: Weak")
    else:
        print("Password strength: Very Weak")


if __name__ == "__main__":
    main()
