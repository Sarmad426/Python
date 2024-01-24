class Name:

    def __init__(self):
        self.name: str = str(input("Enter Your Name: "))

    def greet(self) -> str:
        return f"Welcome {self.name}"


user = Name()
print(user.greet())
