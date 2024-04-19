"""
Python Practice program
"""

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibonacci_series(limit: int) -> None:
    """
    Prints Fibonacci series (0,1,1,2,3,5,8,13)

    Parameters:
    `limit` (int) : limit of fibonacci series

    Returns nothing
    """
    total = 0
    count = 1

    while total < limit:
        print(total)
        prev = count
        count = total
        total += prev


if __name__ == "__main__":
    LIMIT = int(input("Enter fibonacci series limit: "))
    fibonacci_series(LIMIT)
