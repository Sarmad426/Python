# Abstraction in Object-Oriented Programming

Abstraction is one of the key principles in Object-Oriented Programming (OOP). It involves hiding the complex implementation details of a system and only exposing the necessary functionalities to the outside world. Abstraction allows developers to focus on what an object does rather than how it does it. It simplifies the programming model by providing a clear separation between interface and implementation.

## Abstraction in Python

In Python, abstraction can be achieved through the use of classes and methods. By defining classes with methods that represent the behaviors of objects, we can abstract away the implementation details from the users of those objects.

### Code Samples

Here are four different code samples in Python to demonstrate abstraction:

#### 1. Abstract Base Class (ABC) with Abstract Method

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class representing a shape."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

class Square(Shape):
    """Class representing a square."""
    
    def __init__(self, side_length: float) -> None:
        self.side_length = side_length
    
    def area(self) -> float:
        """Calculate the area of the square."""
        return self.side_length ** 2

square = Square(5)
print("Area of the square:", square.area())
```

#### 2. Abstract Property

```python
from abc import ABC, abstractproperty

class Vehicle(ABC):
    """Abstract base class representing a vehicle."""
    
    @abstractproperty
    def max_speed(self) -> float:
        """Maximum speed of the vehicle."""
        pass

class Car(Vehicle):
    """Class representing a car."""
    
    def __init__(self, max_speed: float) -> None:
        self._max_speed = max_speed
    
    @property
    def max_speed(self) -> float:
        return self._max_speed

my_car = Car(200)
print("Max speed of the car:", my_car.max_speed)
```

#### 3. Abstract Class with Concrete Methods

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an animal."""
    
    @abstractmethod
    def sound(self) -> str:
        """Produce the sound of the animal."""
        pass
    
    def move(self) -> str:
        """Describe how the animal moves."""
        return "The animal moves."

class Dog(Animal):
    """Class representing a dog."""
    
    def sound(self) -> str:
        return "Woof!"

dog = Dog()
print(dog.sound())
print(dog.move())
```

#### 4. Interface Abstraction

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    """Interface for payment gateways."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment."""
        pass

class PayPal(PaymentGateway):
    """Class representing the PayPal payment gateway."""
    
    def process_payment(self, amount: float) -> bool:
        """Process a payment using PayPal."""
        print(f"Processing payment of ${amount} via PayPal.")
        return True

class Stripe(PaymentGateway):
    """Class representing the Stripe payment gateway."""
    
    def process_payment(self, amount: float) -> bool:
        """Process a payment using Stripe."""
        print(f"Processing payment of ${amount} via Stripe.")
        return True

paypal_gateway = PayPal()
stripe_gateway = Stripe()

print(paypal_gateway.process_payment(100))
print(stripe_gateway.process_payment(150))
```

These examples demonstrate how abstraction allows us to define interfaces and hide implementation details, providing a clear separation between what an object does and how it does it.
