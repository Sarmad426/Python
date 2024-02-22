"""
Python Program: Sum of Digits of a number
"""


def sum_of_digits_of_num(num: int) -> int:
    """
    Returns the sum of digits of a number for 3 digits < 1000

    Parameter:
    - num (int)

    Returns:
    - sum of digits of `num`
    """
    first = int(num / 100)
    second_third = num % 100

    second = int(second_third / 10)
    third = second_third % 10

    total = first + second + third

    return total


INPUT_NUM = int(input("Enter a number: "))

SUM = sum_of_digits_of_num(INPUT_NUM)

print(SUM)
