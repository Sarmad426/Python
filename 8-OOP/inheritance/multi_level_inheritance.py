"""
Python OOP inheritance program
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

    def __str__(self):
        return f"Person Details: \nName: {self.name}\nAge: {self.age}"


class User(Person):
    """User class with email"""

    def __init__(self, name: str, age: int, email: str):
        super().__init__(name, age)
        self._email = email

    @property
    def email(self) -> str:
        """email getter"""
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    def __str__(self):
        return f"""
User Details:
Name: {self.name}
Age: {self.age}
Email: {self.email}
"""


class Employee(User):
    """
    Employee class with email and department
    """

    def __init__(self, name: str, age: int, email: str, department: str, role: str):
        super().__init__(name, age, email)
        self._department = department
        self._role = role

    @property
    def department(self) -> str:
        """department getter"""
        return self._department

    @department.setter
    def department(self, department: str) -> None:
        self._department = department

    @property
    def role(self) -> str:
        """
        Employee role getter
        """
        return self._role

    @role.setter
    def role(self, role) -> None:
        self._role = role

    def details(self) -> dict[str, str | int]:
        """Returns user details as a dictionary"""

        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "role": self.role,
        }

    def __str__(self):
        return f"""
Employee Details
Name: {self.name}
Age: {self.age}
Email: {self.email}
Department: {self.department}
Role: {self.role}
"""


person = Person("Sarmad", 19)

print(person)

user = User(person.name, person.age, "sarmad@email.com")

print(user)

employee = Employee(user.name, user.age, user.email, "Engineering", "Software Engineer")

print(employee)

print(employee.details())
