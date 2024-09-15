# Decorators:
# A decorator is a function that takes another function as input and adds some functionality to it
# without modifying the original function. Decorators are often used in logging, authentication, and
# performance monitoring by wrapping an existing function with additional behavior.

# Example of a decorator that logs function execution


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' executed successfully")
        return result

    return wrapper


@logger_decorator  # This adds logging to the `add` function
def add(a, b):
    return a + b


# Call the decorated function
add(3, 5)
