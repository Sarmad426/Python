"""
A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward, such as "madam" or "racecar".
"""


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


TEST_STRING = "Madam"
print(f"Is '{TEST_STRING}' a palindrome? {is_palindrome(TEST_STRING)}")


# Another way to check if a string is a palindrome is to reverse the
# string and compare it to the original string.


def is_palindrome_2(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == s[::-1]


print(f"Is '{TEST_STRING}' a palindrome? {is_palindrome_2(TEST_STRING.lower())}")
