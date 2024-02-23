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
            print("*", end="")  # print * and skip new line
            j += 1
        print()  # enter new line after each inner loop iteration


LIMIT = int(input("Enter limit of triangle: "))

triangle(LIMIT)
