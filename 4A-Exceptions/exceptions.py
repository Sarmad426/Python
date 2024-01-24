"""Python Error Handling with try-except-else"""

while True:
    try:
        num: int = int(input("Enter a number: "))
    except ValueError:
        print("You must enter a number!")
    else:
        break

print(num)
