"""
Program checks whether the input number is prime number or not.
"""


def check_prime(num: int) -> bool:
    """
    Checks whether the input number is prime number or not.

    Parameters:
    `num` (int) : number to check

    Returns:
    `bool` : True if the number is prime
    """
    count = 2
    while count < num:
        if num % count == 0:
            return False
        count += 1
    return True


INPUT_NUM = int(input("Enter a number: "))

if check_prime(INPUT_NUM):
    print("Prime number")
else:
    print("Not a prime number")
