"""
Python basic Object Oriented Program

    A simple Person class
"""


class Person:
    """
    A Simple Person class with `name`, `email` and `age`
    """

    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    def greet(self) -> None:
        """
        Greet the user by their name

        Takes no parameters
        """
        print(f"Hi, {self.name}!")


if __name__ == "__main__":
    # Get user input for name, email, and age
    NAME = input("Enter your name: ")
    EMAIL = input("Enter your email: ")

    AGE: int = int(input("Enter your age: "))

    # Create Person object
    user = Person(NAME, EMAIL, AGE)

    # Greet the user
    user.greet()
