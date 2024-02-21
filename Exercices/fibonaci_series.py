"""
Python Practice program
"""

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

total = 0
count = 1

while total < 100:
    prev = count
    count = total
    print(total)
    total += prev
