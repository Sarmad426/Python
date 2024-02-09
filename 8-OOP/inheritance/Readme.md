# Inheritance in Object-Oriented Programming

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a new class (called the subclass or derived class) to inherit attributes and methods from an existing class (called the superclass or base class). Inheritance facilitates code reuse and promotes the creation of a hierarchy of classes with shared characteristics and behaviors. The subclass can extend or override the functionality of the superclass, enabling developers to create specialized classes that inherit and modify the behavior of their parent classes.

## Inheritance in Python

In Python, inheritance is implemented using the syntax `class Subclass(BaseClass):`. The subclass inherits all attributes and methods of the base class and can define additional attributes or override existing methods as needed. Python supports single inheritance, meaning a class can inherit from only one superclass, but it also supports multiple inheritance, where a class can inherit from multiple superclasses.

### Code Samples

Here are two code samples in Python to demonstrate inheritance:

#### 1. Single Inheritance

```python
class Animal:
    """Base class representing an animal."""
    
    def speak(self) -> str:
        """Speak like an animal."""
        return "Some generic animal sound."

class Dog(Animal):
    """Subclass representing a dog."""
    
    def speak(self) -> str:
        """Speak like a dog."""
        return "Woof!"

class Cat(Animal):
    """Subclass representing a cat."""
    
    def speak(self) -> str:
        """Speak like a cat."""
        return "Meow!"

# Creating objects of subclasses
dog = Dog()
cat = Cat()

# Calling methods from the base class
print("Generic animal sound:", dog.speak())  # Output: Woof!
print("Generic animal sound:", cat.speak())  # Output: Meow!
```

#### 2. Multiple Inheritance

```python
class Flyable:
    """Mixin class representing flyable objects."""
    
    def fly(self) -> str:
        """Fly like a flyable object."""
        return "Flying high."

class Animal:
    """Base class representing an animal."""
    
    def speak(self) -> str:
        """Speak like an animal."""
        return "Some generic animal sound."

class Bird(Animal, Flyable):
    """Subclass representing a bird."""
    
    def speak(self) -> str:
        """Speak like a bird."""
        return "Tweet!"

# Creating object of subclass with multiple inheritance
bird = Bird()

# Calling methods from both base classes
print("Generic animal sound:", bird.speak())  # Output: Tweet!
print("Flyable object behavior:", bird.fly())  # Output: Flying high.
```

These examples illustrate how inheritance allows subclasses to inherit attributes and methods from their superclasses, promoting code reuse and enabling the creation of specialized classes with shared characteristics and behaviors.
