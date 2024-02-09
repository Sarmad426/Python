# Encapsulation in Object-Oriented Programming

Encapsulation is another fundamental principle in Object-Oriented Programming (OOP). It involves bundling the data (attributes) and methods (behaviors) that operate on the data into a single unit, called a class. Encapsulation allows for data hiding, where the internal state of an object is not directly accessible from outside the class. Instead, access to the data is controlled through methods, which are often referred to as getters and setters. This helps in achieving data abstraction and protection.

## Encapsulation in Python

In Python, encapsulation is typically implemented using classes. By defining attributes as private (prefixed with double underscores `__`) and providing public methods to access or modify these attributes, encapsulation can be achieved. This ensures that the internal state of an object remains hidden from the outside world and can only be accessed or modified through well-defined interfaces.

### Code Samples

Here are four different code samples in Python to demonstrate encapsulation:

#### 1. Private Attributes with Getter and Setter Methods

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

#### 2. Using Property Decorators

```python
class Car:
    """Class representing a car."""
    
    def __init__(self, make: str, model: str) -> None:
        self.__make = make
        self.__model = model
    
    @property
    def make(self) -> str:
        """Get the make of the car."""
        return self.__make
    
    @make.setter
    def make(self, make: str) -> None:
        """Set the make of the car."""
        self.__make = make
    
    @property
    def model(self) -> str:
        """Get the model of the car."""
        return self.__model
    
    @model.setter
    def model(self, model: str) -> None:
        """Set the model of the car."""
        self.__model = model

my_car = Car("Toyota", "Camry")
print("Make:", my_car.make)
print("Model:", my_car.model)

my_car.make = "Honda"
my_car.model = "Accord"
print("Updated Make:", my_car.make)
print("Updated Model:", my_car.model)
```

#### 3. Encapsulation with Private Methods

```python
class Calculator:
    """Class representing a simple calculator."""
    
    def __init__(self) -> None:
        self.__result = 0
    
    def __add(self, num: int) -> None:
        """Private method to add a number to the result."""
        self.__result += num
    
    def __subtract(self, num: int) -> None:
        """Private method to subtract a number from the result."""
        self.__result -= num
    
    def add_numbers(self, num1: int, num2: int) -> None:
        """Public method to add two numbers."""
        self.__add(num1)
        self.__add(num2)
    
    def subtract_numbers(self, num1: int, num2: int) -> None:
        """Public method to subtract two numbers."""
        self.__subtract(num1)
        self.__subtract(num2)
    
    def get_result(self) -> int:
        """Get the current result."""
        return self.__result

calculator = Calculator()
calculator.add_numbers(10, 5)
print("Result after addition:", calculator.get_result())

calculator.subtract_numbers(3, 2)
print("Result after subtraction:", calculator.get_result())
```

#### 4. Encapsulation with Class Composition

```python
class Engine:
    """Class representing an engine."""
    
    def start(self) -> None:
        """Start the engine."""
        print("Engine started.")

class Car:
    """Class representing a car."""
    
    def __init__(self) -> None:
        self.__engine = Engine()
    
    def start_engine(self) -> None:
        """Start the car's engine."""
        self.__engine.start()

my_car = Car()
my_car.start_engine()
```

These examples illustrate how encapsulation helps in hiding the internal state of objects and provides controlled access to them, thus preventing direct manipulation and ensuring data integrity.
