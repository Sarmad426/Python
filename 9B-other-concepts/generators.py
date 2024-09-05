# Generators:
# A generator is a special type of iterator in Python, which allows you to iterate over a sequence of values 
# lazily (i.e., one at a time), instead of storing the entire sequence in memory. Generators are defined using 
# the `yield` keyword instead of `return`. Each call to the generator's `__next__()` method or `next()` function 
# resumes the function from where it last left off, yielding the next value.


# Example of a generator that yields numbers from 1 to n

def number_generator(n):
    for i in range(1, n + 1):
        yield i

# Create a generator object
gen = number_generator(5)

# Iterate over the generated values
for num in gen:
    print(num)  # Output: 1 2 3 4 5 (one at a time)
