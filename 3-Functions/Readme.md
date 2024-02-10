# Functions

A function is a block of code that performs an operation. Functions reduce code redundancy and makes code clean and concise.

## Types of functions

- Built in functions
- User defined functions

### Built-in functions

There are other functions that comes with the language, these functions are called **built-in functions**. There are functions like `sorted()` that sorts a list or a tuple, there is `filter()` that filters values based on a certain criteria.

### User-defined functions

These are functions that the programmer creates to implement a logic.

## Difference between function arguments vs parameters

### Function Parameters

These are the variables listed in the function definition. They act as placeholders for the values that are to be supplied to the function when it is called. Parameters are essentially the names listed in the function definition.

```py

def greet(name:str) -> str:
    return f"Asslamo Alliakum {name}"

```

`name` is the function parameter.

### Function Arguments

These are the actual values that are passed to the function when it is called. These values are assigned to the corresponding parameters inside the function. Arguments are the actual data or variables passed into the function when calling it.

```py
greet("Sarmad")
```

value 'Sarmad' is the function argument.

## Recursion

A function calling itself recursively (again & again) until a particular condition breaks the function.

## Lambda function in python

Lambda functions, also known as anonymous functions, are small, unnamed functions defined using the `lambda` keyword. They are typically used for short-term operations where a full function definition is not necessary. Lambda functions can take any number of arguments but can only have one expression.
