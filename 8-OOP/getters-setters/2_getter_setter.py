"""
Python OOP getter & setter program
"""


class Person:
    """
    Person class with name and email
    """

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        """Person name getter"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        """Person name getter"""
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def details(self) -> dict[str, str | int]:
        """
        Returns user details as a dictionary
        """
        return {"name": self.name, "age": self.age}


person = Person("Sarmad", 19)

print(person.details())

person.name = "Kamran"
person.age = 24

print(person.details())
