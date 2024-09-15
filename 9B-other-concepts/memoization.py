"""
Memoization in python
"""


def memoize(func):
    cache = {}  # Store results in a cache

    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def expensive_function(x):
    print(f"Calculating result for {x}")
    return x * x  # Example of an expensive calculation


# First call (expensive calculation)
print(expensive_function(5))  # Output: Calculating result for 5, then 25

# Second call with same argument (returns cached result)
print(expensive_function(5))  # Output: Returning cached result for 5, then 25
