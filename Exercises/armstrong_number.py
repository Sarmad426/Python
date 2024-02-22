"""
Program checks whether the input number is armstrong number or not.
Armstrong numbers: $(153,371,407)$
"""

from helper_methods.power_func import power_func


def check_armstrong(num: int) -> bool:
    """
    Checks whether the input number is armstrong number or not.

    Parameters:
    `num` (int) : number to check

    Returns:
    `bool` : True if the number is armstrong
    """
    power = len(str(num))
    temp = num
    total = 0
    while temp >= 1:
        digit = temp % 10
        total += power_func(digit, power)
        temp = int(temp / 10)
    if total == num:
        return True
    return False


INPUT_NUM = int(input("Enter a number: "))

if check_armstrong(INPUT_NUM):
    print("Armstrong number")
else:
    print("Not an armstrong number")
