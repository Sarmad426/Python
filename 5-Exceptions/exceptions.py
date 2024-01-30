"""Python Error Handling with try-except-else"""


def main() -> None:
    num: int = get_num()
    print(f"num: {num}")


def get_num() -> int:
    while True:
        try:
            num: int = int(input("Enter a number: "))
            return num
        except ValueError:
            pass


main()
