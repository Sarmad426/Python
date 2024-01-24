"""Python Error Handling with try-except-else"""

while True:
    try:
        num: int = int(input("Enter a number: "))
        break
    except ValueError:
        print("You must enter a number!")

print(num)
