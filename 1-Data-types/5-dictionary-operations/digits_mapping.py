"""
Digits mapping exercise

Mapped phone number digits to english alphabets

"""


def map_digits(phone_num: str, data_set: dict[str, str]) -> str:
    """
    Maps Numeric digits to english alphabets

    Parameters:
    - phone_num (str): Phone number
    - data_set (dict[str, str]) : Dictionary data set

    Return type: str
        returns the digit corresponding to the alphabets
    """
    mapped_digits = ""

    for char in phone_num:
        mapped_digits += data_set.get(char, "") + " "

    return mapped_digits


def main() -> None:
    """
    Main function

    Initialized the Characters dictionary
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
        "0": "Zero",
    }

    phone_num = input("Phone Number: ")

    output: str = map_digits(phone_num, characters)

    print(output)


if __name__ == "__main__":
    main()
