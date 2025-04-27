"""
Secret token generator
"""

import os
import binascii

def generate_secret_key(length=32):
    """Generate a secure secret key."""
    return binascii.hexlify(os.urandom(length)).decode()

# Generate a 32-byte secure secret key
secret_key = generate_secret_key()
print("Generated Secret Key:", secret_key)