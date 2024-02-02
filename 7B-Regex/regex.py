import re

# Example 3: Matching an email address
pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
email = str(input("Enter your email address: "))
result = pattern.search(email)
print(result.group())  # Output: support@example.com
