# Python Unit Tests

## Unit Tests

A unit is the smallest testable part of an application, typically a function, method, or class. The goal of unit testing is to validate that each unit of the software performs as designed.

In the context of Python, unit testing is often done using the built-in **unittest** module or third-party libraries like **pytest**.

Unit testing with python library **pytest**.

Install pytest.

```pip
%pip install pytest
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

To test the code using *pytest*.

instead of executing file with python,
execute it with **pytest**.

Here is an example for the `unit-tests.py` file in this directory.

`pytest 6B-unit-tests/unit-tests.py`
