# Polymorphism in Object-Oriented Programming

Polymorphism is a key concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables methods to do different things based on the object that they are acting upon. Polymorphism allows for flexibility and extensibility in the design of software systems, as it allows for code reuse and enables writing code that can work with objects of various types without needing to know their specific classes.

## Polymorphism in Python

In Python, polymorphism is achieved through method overriding and method overloading. Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. Method overloading, however, is not directly supported in Python as it is in languages like Java or C++, but Python offers a flexible way to achieve similar functionality through default arguments or variable-length arguments.

### Code Samples

Here are two code samples in Python to demonstrate polymorphism:

#### 1. Method Overriding

```python
class Animal:
    """Class representing an animal."""
    
    def sound(self) -> str:
        """Produce the sound of the animal."""
        return "Some generic animal sound."

class Dog(Animal):
    """Class representing a dog."""
    
    def sound(self) -> str:
        """Produce the sound of the dog."""
        return "Woof!"

class Cat(Animal):
    """Class representing a cat."""
    
    def sound(self) -> str:
        """Produce the sound of the cat."""
        return "Meow!"

def make_sound(animal: Animal) -> None:
    """Make the given animal sound."""
    print(animal.sound())

# Polymorphic behavior based on object types
dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
```

#### 2. Duck Typing

```python
class Bird:
    """Class representing a bird."""
    
    def fly(self) -> str:
        """Fly like a bird."""
        return "Flying high."

class Airplane:
    """Class representing an airplane."""
    
    def fly(self) -> str:
        """Fly like an airplane."""
        return "Soaring through the sky."

def lift_off(entity):
    """Make the given entity fly."""
    return entity.fly()

# Polymorphic behavior based on methods
bird = Bird()
airplane = Airplane()

print(lift_off(bird))      # Output: Flying high.
print(lift_off(airplane))  # Output: Soaring through the sky.
```

These examples demonstrate how polymorphism allows different objects to be treated uniformly through a common interface, enabling code reuse, flexibility, and extensibility in software design.
