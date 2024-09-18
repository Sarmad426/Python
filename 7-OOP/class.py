"""
Python basic Object Oriented Program
"""


class Person:
    """
    A class to represent a person.

    Attributes:
        name (str): The name of the person.
        email (str): The email address of the person.
        age (int): The age of the person.
    """

    def __init__(self, name: str, email: str, age: int):
        """
        Constructor for the Person class.

        Parameters:
            name (str): The name of the person.
            email (str): The email address of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.email = email
        self.age = age

    def greet(self) -> None:
        """
        Greet the user by their name
        """
        print(f"Hi, {self.name.capitalize()}!")


if __name__ == "__main__":

    NAME = input("Enter your name: ")
    EMAIL = input("Enter your email: ")
    AGE: int = int(input("Enter your age: "))

    user = Person(NAME, EMAIL, AGE)

    user.greet()
