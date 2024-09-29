"""
Gets user input and validates it
"""


def get_string_input(label: str) -> str | None:
    """
    Gets string input and validates it
    """
    try:
        string = input(f"{label}: ")
        string.strip()
        if not string or not string.isascii():
            raise ValueError
        return string
    except ValueError:
        print("Invalid input!")
    return None


def get_int_input(label: str) -> int | None:
    """
    Gets string input and validates it
    """
    try:
        num = int(input(f"{label}: "))
        if not num:
            raise ValueError
        return num
    except ValueError:
        print("Invalid input!")
    return None


print(get_string_input("Enter name"))
print(get_int_input("Enter age"))
