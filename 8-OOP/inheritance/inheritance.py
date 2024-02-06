"""
Basic Class objects inheritance
"""


class Person:
    """
    Person class with name, email and age
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class Professor(Person):
    """
    Professor class inheriting `Person` class and having a `Subject` field.
    """

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"Professor {self.name} teaches {self.subject}"


person = Person("Sarmad", 19)

professor = Professor("Kamran", 26, "Computer Science")

print(professor)
