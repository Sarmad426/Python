"""
Left triangle shape
"""


def triangle(limit: int):
    """
    Prints left triangle
    """
    for i in range(limit):
        j = 0
        while j < i:
            print("*", end="")
            j += 1
        print()


LIMIT = int(input("Enter limit of triangle: "))

triangle(LIMIT)
