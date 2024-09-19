# Inheritance in Object-Oriented Programming

**Inheritance** is a fundamental concept in **Object-Oriented Programming (OOP)** that allows a new class (called the subclass or derived class) to inherit attributes and methods from an existing class (called the superclass or base class). Inheritance facilitates code reuse and promotes the creation of a hierarchy of classes with shared characteristics and behaviors. The subclass can extend or override the functionality of the superclass, enabling developers to create specialized classes that inherit and modify the behavior of their parent classes.

## Inheritance in Python

In Python, inheritance is implemented using the syntax `class Subclass(BaseClass):`. The subclass inherits all attributes and methods of the base class and can define additional attributes or override existing methods as needed. Python supports single inheritance, meaning a class can inherit from only one superclass, but it also supports multiple inheritance, where a class can inherit from multiple superclasses.

### Code Samples

Here are two code samples in Python to demonstrate inheritance:

### 1. Single Inheritance

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

### 2. Multiple Inheritance

Multiple inheritance refers to the ability of a class to inherit attributes and methods from
more than one parent class. In other words, a subclass can inherit from multiple superclasses.
This means that the subclass has access to all the methods and attributes of each of its
parent classes. However, multiple inheritance can lead to complex class hierarchies and
potential issues such as the diamond problem, where the same method is inherited from two
different parent classes. Python supports multiple inheritance, but it requires careful design
to avoid such issues.

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

### 3. Multi-level Inheritance

Multi-level inheritance, refers to a situation where a class inherits from another class, and then another class inherits from this derived class. This creates a hierarchical relationship between classes, where each subsequent class adds more specific attributes or behavior to the hierarchy. It is a simpler form of inheritance compared to multiple inheritance, as there is only one direct parent class for each subclass. This hierarchy can be seen as a chain of classes, with each link representing a level of inheritance. Multi-level inheritance is commonly used to model real-world relationships where subclasses specialize or refine the behavior of their parent classes.

```py
# Base class
class Animal:
    def speak(self):
        return "Generic animal sound"

# Derived class inheriting from Animal
class Bird(Animal):
    def speak(self):
        return "Tweet!"

    def fly(self):
        return "Flying high."

# Further derived class inheriting from Bird
class Parrot(Bird):
    def speak(self):
        return "Parrot says hello!"

# Creating object of the most derived class
parrot = Parrot()

# Calling methods from all levels of the hierarchy
print("Parrot sound:", parrot.speak())  # Output: Parrot says hello!
print("Flyable object behavior:", parrot.fly())  # Output: Flying high.
```
