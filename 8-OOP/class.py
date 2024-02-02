"""Module to greet user by their name"""


class Name:
    """Class representing name of a person"""

    def __init__(self) -> None:
        self.name = str(input("Enter Your Name: "))

    def greet(self) -> str:
        """Greet the user"""
        return f"Welcome {self.name}"


user = Name()
print(user.greet())
