"""
Python basic Object Oriented Program

    A simple Person class
"""

import re


class Person:
    """
    A Simple Person class with `name`, `email` and `age`
    """

    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates user email by `REGEX`
        """
        email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        return bool(re.match(email_pattern, email))

    @staticmethod
    def validate_age(age: int) -> bool:
        """
        Validates user age

        Age must be greater than 0.\n
        Takes one parameter `(age:int)` and returns the boolean `(age > 0)`
        """
        # Age validation (positive integer)
        return age > 0

    def greet(self) -> None:
        """
        Greet the user by their name

        Takes no parameters
        """
        print(f"Hello, {self.name}!")


if __name__ == "__main__":
    # Get user input for name, email, and age
    NAME = input("Enter your name: ")
    EMAIL = input("Enter your email: ")

    # Validate email input
    while not Person.validate_email(EMAIL):
        print("Invalid email format. Please enter a valid email.")
        email = input("Enter your email: ")

    age: int = int(input("Enter your age: "))

    # Validate age input
    while not Person.validate_age(int(age)):
        print("Invalid age. Please enter a valid positive integer age.")
        age = int(input("Enter your age: "))

    # Create Person object
    user = Person(NAME, EMAIL, age)

    # Greet the user
    user.greet()
