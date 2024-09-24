"""
Python program to convert phone number to words
"""

characters: dict[str, str] = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}


def number_to_words(digits: str) -> str:
    """
    Converts number to english alphabets
    """

    phone_num = ""
    for char in digits:
        phone_num += characters.get(char, "") + " "

    return phone_num


print(number_to_words(input("Enter phone number: ")))
