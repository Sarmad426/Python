import re

class Person:
    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    @staticmethod
    def validate_email(email: str) -> bool:
        # Simple email validation using regex
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(re.match(email_pattern, email))

    @staticmethod
    def validate_age(age: int) -> bool:
        # Age validation (positive integer)
        return age > 0

    def greet(self) -> None:
        print(f"Hello, {self.name}!")

if __name__ == "__main__":
    # Get user input for name, email, and age
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    # Validate email input
    while not Person.validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        email = input("Enter your email: ")

    age = input("Enter your age: ")

    # Validate age input
    while not age.isdigit() or not Person.validate_age(int(age)):
        print("Invalid age. Please enter a valid positive integer age.")
        age = input("Enter your age: ")

    # Create Person object
    user = Person(name, email, int(age))

    # Greet the user
    user.greet()
