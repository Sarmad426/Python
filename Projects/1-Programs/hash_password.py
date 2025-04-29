"""
Password hasher
"""

import hashlib


def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(input_password, stored_hash):
    """Checks if the input password matches the stored hash."""
    return hash_password(input_password) == stored_hash


def main():
    """
    Main function
    """
    original_password = input("Enter the original password: ")
    hashed_password = hash_password(original_password)
    print(f"Password hashed: {hashed_password}")

    entered_password = input("Enter the password to verify: ")

    if check_password(entered_password, hashed_password):
        print("Password is valid.")
    else:
        print("Invalid password.")


if __name__ == "__main__":
    main()
