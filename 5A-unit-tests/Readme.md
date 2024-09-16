# Python Unit Tests

## Unit Tests

A unit is the smallest testable part of an application, typically a function, method, or class. The goal of unit testing is to validate that each unit of the software performs as designed.

In the context of Python, unit testing is often done using the built-in **unittest** module or third-party libraries like **pytest**.

Unit testing with python library **pytest**.

Install pytest.

```bash
pip install pytest
```

We use the python `assert` keyword for this purpose.

## Assert Keyword

In Python, the `assert` keyword is used to test a condition as a debugging aid. It takes an expression, and if the expression is `False`, it raises an `AssertionError` exception with an optional error message. If the expression is `True`, the program continues execution.

Here's a simple example:

```python
x = 10

assert x > 0, "x should be a positive number"
```

In this example, if `x` is not greater than 0, the `assert` statement will raise an `AssertionError` with the message "x should be a positive number." This is particularly useful during development to catch logical errors or unexpected conditions early in the code. However, it's important to note that using `assert` for data validation in production code is not recommended, as it can be disabled globally, and unexpected failures may lead to security vulnerabilities.

To test the code using `pytest`.

instead of executing file with python,
execute it with `pytest`.

**Run tests:**

Here is an example for the `unit_tests.py` file in this directory.

`pytest 6B-unit-tests/unit_tests.py`

### Using `unittest`

The `unittest` module is part of the Python standard library and provides a more comprehensive testing framework. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and more.

Here's an example of using `unittest`:

```py
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()
```

In this example, we define a simple `add` function and a `TestAdd` class that inherits from `unittest.TestCase`. We then define a test method `test_add` that uses various `assert` methods provided by `unittest.TestCase` to check the behavior of the `add` function.

**Run tests:**

To run the tests, you can execute the script directly, and `unittest` will discover and run the tests:

```bash
python test_add.py
```
