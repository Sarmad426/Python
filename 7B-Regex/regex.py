"""
Email Validator program using REGEX.
"""

import re

# Matching an email address

pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
EMAIL: str = str(input("Enter your email address: "))
result = pattern.search(EMAIL)
print(result.group())
