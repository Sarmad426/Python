"""Python Error Handling with try-except-else"""


def main() -> None:
    """
    This function serves as the entry point of the program.
    It prompts the user to enter a number and prints the number.
    """
    num: int = get_num()
    print(f"num: {num}")


def get_num() -> int:
    """
    Prompts the user to enter a number and returns the entered number.
    Returns:
        int: The number entered by the user.
    Raises:
        ValueError: If the user enters a value that cannot be converted to an integer.
    """
    while True:
        try:
            num: int = int(input("Enter a number: "))
            return num
        except ValueError:
            pass


main()
