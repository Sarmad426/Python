
# Positional Argument packing
def add_numbers(*args):
    # *args allows the function to accept any number of positional arguments
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)  # Passing multiple arguments
print(result)  # Output: 15

# Unpacking Iterables

def greet(name1, name2, name3):
    # Function expects three arguments
    print(f"Hello, {name1}, {name2}, and {name3}!")

names = ["Alice", "Bob", "Charlie"]
greet(*names)  # Unpacking the list into separate arguments
# Output: Hello, Alice, Bob, and Charlie!

# Keyword argument packing

def display_info(**kwargs):
    # **kwargs allows the function to accept any number of keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Sarmad", age=20, location="Asia")
# Output:
# name: Sarmad
# age: 20
# location: Asia

# Unpacking dictionaries

def create_user(username, email, age):
    # Function expects three keyword arguments
    print(f"Username: {username}, Email: {email}, Age: {age}")

user_data = {"username": "sarmad123", "email": "sarmad@example.com", "age": 25}
create_user(**user_data)  # Unpacking the dictionary into keyword arguments
# Output: Username: sarmad123, Email: sarmad@example.com, Age: 25

# Mixed positional and keyword arguments

def process_data(a, b, *args, **kwargs):
    # a and b are regular positional arguments
    # *args captures additional positional arguments
    # **kwargs captures additional keyword arguments
    print(f"a: {a}, b: {b}")
    print(f"Additional positional args: {args}")
    print(f"Additional keyword args: {kwargs}")

process_data(1, 2, 3, 4, x=10, y=20)
# Output:
# a: 1, b: 2
# Additional positional args: (3, 4)
# Additional keyword args: {'x': 10, 'y': 20}
