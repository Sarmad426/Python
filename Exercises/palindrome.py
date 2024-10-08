"""
A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward, such as "madam" or "racecar".
"""


def is_palindrome(string: str) -> bool:
    """Checks weather the string is palindrome or not

    Args:
        string (str): string to be checked for palindrome

    Returns:
        bool: `string` is palindrome or not
    """
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1

    return True


TEST_STRING = "Madam"
print(f"Is '{TEST_STRING}' a palindrome? {is_palindrome(TEST_STRING)}")


# Another way to check if a string is a palindrome is to reverse the
# string and compare it to the original string.


def is_palindrome_2(s: str) -> bool:
    """Checks weather the string is palindrome or not

    Args:
        string (str): string to be checked for palindrome

    Returns:
        bool: `string` is palindrome or not
    """
    return s == s[::-1]


print(f"Is '{TEST_STRING}' a palindrome? {is_palindrome_2(TEST_STRING.lower())}")
