"""
Sum of digits of a number
"""


def sum_digits(number):
    """
    Sum the digits of a given number

    Args:
        number (int): The number to sum the digits of

    Returns:
        int: The sum of the digits of the given number
    """
    return sum(int(digit) for digit in str(abs(number)))


def main():
    """
    Main function to run the program
    """
    while True:
        try:
            user_input = input("Enter an integer: ")
            number = int(user_input)
            result = sum_digits(number)
            print(f"Sum of digits: {result}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
