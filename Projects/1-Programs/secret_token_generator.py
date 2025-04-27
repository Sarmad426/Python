"""
Secret token generator
"""

import secrets


def generate_secret_key(length=32):
    """
    Generates a secret key with the specified length.

    Args:
        length (int): The length of the secret key (default is 32).

    Returns:
        str: A randomly generated secret key.
    """
    return secrets.token_hex(length)


# Generate a secret key
secret_key = generate_secret_key()
print(f"Your secret key: {secret_key}")
