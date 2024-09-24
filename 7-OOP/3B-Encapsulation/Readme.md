# Encapsulation in Object-Oriented Programming

Encapsulation is another fundamental principle in Object-Oriented Programming (OOP). It involves bundling the data (attributes) and methods (behaviors) that operate on the data into a single unit, called a class. Encapsulation allows for data hiding, where the internal state of an object is not directly accessible from outside the class. Instead, access to the data is controlled through methods, which are often referred to as getters and setters. This helps in achieving data abstraction and protection.

## Encapsulation in Python

In Python, encapsulation is typically implemented using classes. By defining attributes as private (prefixed with double underscores `__`) and providing public methods to access or modify these attributes, encapsulation can be achieved. This ensures that the internal state of an object remains hidden from the outside world and can only be accessed or modified through well-defined interfaces.

### Code Example

#### Private Attributes with Getter and Setter Methods

```python
class Person:
    """Class representing a person."""
    
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age
    
    def get_name(self) -> str:
        """Get the name of the person."""
        return self.__name
    
    def set_name(self, name: str) -> None:
        """Set the name of the person."""
        self.__name = name
    
    def get_age(self) -> int:
        """Get the age of the person."""
        return self.__age
    
    def set_age(self, age: int) -> None:
        """Set the age of the person."""
        self.__age = age

person = Person("Alice", 30)
print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Bob")
person.set_age(25)
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
```
