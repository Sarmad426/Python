# Operator Overloading

Operator overloading is a feature in object-oriented programming languages that allows developers to redefine the behavior of operators (such as +, -, *, /, etc.) for user-defined classes. This means you can define custom behavior for operators when they are used with objects of your class.

In Python, operator overloading is achieved by providing special methods with predefined names. These methods are called when instances of a class are used with operators.

Here's a brief explanation and examples at different levels of complexity:

## Simple Operator Overloading program

Let's create a class `Point` to represent a point in 2D space. We'll overload the `+` operator to add two points together.

```python

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

# Usage
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print(f"Result: ({result.x}, {result.y})")  # Output: Result: (4, 6)
```

### Medium Level Program

Let's extend the example to overload the `==` operator to check if two points are equal.

```python
from typing import Tuple

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

# Usage
point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)  # Output: True
```

### Difficult Level Program

Let's overload the `*` operator to implement scalar multiplication for a vector class.

```python
from typing import List

class Vector:
    def __init__(self, values: List[float]):
        self.values = values
    
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector([x * scalar for x in self.values])
    
    def __rmul__(self, scalar: float) -> 'Vector':  # handles scalar * vector
        return self * scalar

# Usage
vec = Vector([1, 2, 3])
result1 = vec * 2
result2 = 3 * vec
print(result1.values)  # Output: [2, 4, 6]
print(result2.values)  # Output: [3, 6, 9]
```

These examples demonstrate how to overload operators in Python using special methods (`__add__`, `__eq__`, `__mul__`, etc.) and how they can be used to provide custom behavior for user-defined classes.
