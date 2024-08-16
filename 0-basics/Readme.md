# Python Cheat Sheet

Python is a versatile, high-level programming language known for its readability and simplicity. It's widely used in web development, data analysis, artificial intelligence, machine learning, and automation. Python's extensive libraries and supportive community make it a popular choice for both beginners and experienced developers. Its ability to handle complex tasks with minimal code has cemented its importance in today's tech-driven world.

## Table of Contents

- [Python Cheat Sheet](#python-cheat-sheet)
  - [Table of Contents](#table-of-contents)
  - [Variables](#variables)
  - [Comments](#comments)
  - [Receiving Input](#receiving-input)
  - [Strings](#strings)
  - [Arithmetic Operations](#arithmetic-operations)
  - [If Statements](#if-statements)
  - [Comparison Operators](#comparison-operators)
  - [While Loops](#while-loops)
  - [For Loops](#for-loops)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Functions](#functions)
  - [Exceptions](#exceptions)
  - [Classes](#classes)
  - [Inheritance](#inheritance)
  - [Modules](#modules)
  - [Packages](#packages)
  - [Python Standard Library](#python-standard-library)
  - [Pypi](#pypi)

## Variables

We use variables to temporarily store data in the computer’s memory.

```python
price = 10
rating = 4.9
course_name = 'Python for Beginners'
is_published = True
```

- `price` is an integer.
- `rating` is a float.
- `course_name` is a string.
- `is_published` is a boolean.

## Comments

We use comments to add notes to our code.

```python
# This is a comment and it won’t get executed.
# Our comments can be multiple lines.
```

## Receiving Input

We can receive input from the user by calling the `input()` function.

```python
birth_year = int(input('Birth year: '))
```

The `input()` function always returns data as a string.

## Strings

We can define strings using single (`' '`) or double (`" "`) quotes.

```python
course = 'Python for Beginners'
course[0]  # returns the first character
course[-1] # returns the last character
course[1:5] # returns 'ytho'
```

We can use formatted strings to dynamically insert values into our strings.

```python
name = 'Mosh'
message = f'Hi, my name is {name}'
```

## Arithmetic Operations

```python
+
-
*
/  # returns a float
// # returns an int
%  # returns the remainder of division
** # exponentiation
```

Operator precedence:

1. Parenthesis
2. Exponentiation
3. Multiplication / Division
4. Addition / Subtraction

## If Statements

```python
if is_hot:
    print("hot day")
elif is_cold:
    print("cold day")
else:
    print("beautiful day")
```

## Comparison Operators

```python
a > b
a >= b
a < b
a <= b
a == b
a != b
```

## While Loops

```python
i = 1
while i < 5:
    print(i)
    i += 1
```

## For Loops

```python
for i in range(1, 5):
    print(i)
```

## Lists

```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # adds 6 to the end
numbers.remove(6) # removes 6
numbers.sort()    # sorts the list
```

## Tuples

Tuples are immutable and are like read-only lists.

```python
coordinates = (1, 2, 3)
x, y, z = coordinates
```

## Dictionaries

We use dictionaries to store key/value pairs.

```python
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] # returns "John Smith"
```

## Functions

We use functions to break up our code into small chunks.

```python
def greet_user(name):
    print(f"Hi {name}")

greet_user("John")
```

## Exceptions

Exceptions are errors that crash our programs.

```python
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
except ValueError:
    print('Not a valid number')
except ZeroDivisionError:
    print('Age cannot be 0')
```

## Classes

We use classes to define new types.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

point1 = Point(10, 5)
point1.move()
```

## Inheritance

Inheritance is a technique to remove code duplication.

```python
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

dog = Dog()
dog.walk() # inherited from Mammal
dog.bark() # defined in Dog
```

## Modules

A module is a file with some Python code.

```python
import converters
converters.kg_to_lbs(5)

from converters import kg_to_lbs
kg_to_lbs(5)
```

## Packages

A package is a directory with `__init__.py` in it.

```python
from ecommerce import sales
sales.calc_shipping()

from ecommerce.sales import calc_shipping
calc_shipping()
```

## Python Standard Library

Python comes with a huge library of modules for performing common tasks.

```python
import random
random.random()    # returns a float between 0 and 1
random.randint(1, 6) # returns an int between 1 and 6

import datetime
print(datetime.datetime.now())  # returns the current date and time
```

## Pypi

Python Package Index (pypi.org) is a directory of Python packages published by Python developers around the world.

```python
pip install openpyxl
pip uninstall openpyxl
```
