"""Python Error Handling with try-except-finally"""

try:
    num: int = int(input("Enter a number: "))
except ValueError:
    print("You must enter a number!")
else:
    print(num)
