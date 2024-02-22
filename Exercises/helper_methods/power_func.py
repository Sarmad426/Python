"""
Program to give the power of a value
"""


def power_func(num: int, power_digit: int) -> int:
    """
    Returns the power of the given number

    Parameters:
    - `num` (int) : number for power
    - `pow` (int) : power digit

    Returns the power of the given number
    """
    TEMP = num
    count = power_digit
    while count > 1:
        count -= 1
        num *= TEMP
    return num


if __name__ == "__main__":

    NUM_INPUT = int(input("Enter a number: "))
    POWER_INPUT = int(input("Enter power number: "))

    POWER = power_func(NUM_INPUT, POWER_INPUT)

    print(POWER)
