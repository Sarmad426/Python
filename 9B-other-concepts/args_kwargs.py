"""
Python args and keyword args
"""

from typing import Any, Dict


# Positional Argument packing
def add_numbers(*args: int) -> int:
    """
    Accepts any number of positional arguments and returns their sum.
    """
    # *args allows the function to accept any number of positional arguments
    return sum(args)


result = add_numbers(1, 2, 3, 4, 5)  # Passing multiple arguments
print(result)


# Unpacking Iterables
def greet(name1: str, name2: str, name3: str) -> None:
    """
    Greet three people by name.
    """
    # Function expects three arguments
    print(f"Hello, {name1}, {name2}, and {name3}!")


names = ["Alice", "Bob", "Charlie"]
greet(*names)  # Unpacking the list into separate arguments


# Keyword argument packing
def display_info(**kwargs: Any) -> None:
    """
    Display info using the `kwargs`
    """
    # **kwargs allows the function to accept any number of keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Sarmad", age=20, location="Asia")

# Specify the exact structure using Dict
user_data: Dict[str, Any] = {
    "username": "sarmad123",
    "email": "sarmad@example.com",
    "age": 25,
}


# Unpacking dictionaries
def create_user(username: str, email: str, age: int) -> None:
    """
    Unpacking dictionary
    """
    # Function expects three keyword arguments
    print(f"Username: {username}, Email: {email}, Age: {age}")


create_user(**user_data)  # Unpacking the dictionary into keyword arguments


# Mixed positional and keyword arguments
def process_data(a: int, b: int, *args: int, **kwargs: Any) -> None:
    """
    Mixed positional (`*args`) and keyword arguments (`**kwargs`)
    """
    # a and b are regular positional arguments
    # *args captures additional positional arguments
    # **kwargs captures additional keyword arguments
    print(f"a: {a}, b: {b}")
    print(f"Additional positional args: {args}")
    print(f"Additional keyword args: {kwargs}")


process_data(1, 2, 3, 4, x=10, y=20)
