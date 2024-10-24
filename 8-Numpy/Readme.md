# NumPy

NumPy is a Python library that stands for Numerical Python. It is a fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. NumPy is widely used in various fields such as data analysis, machine learning, image processing, and more.

## Installation

To install NumPy, you can use the following command:

```bash
%pip install numpy
```

Make sure you have Python and pip installed on your system before running this command.

## Usage

To use NumPy in your Python code, you need to import the library. Here's an example:

```python
import numpy as np
```

Now you can use NumPy functions and features in your code. Here are a few examples:

```python
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform mathematical operations on arrays
arr2 = arr + 5
arr3 = np.sin(arr)

# Perform array operations
arr4 = np.concatenate((arr, arr2))

# Perform array computations
mean = np.mean(arr)
max_value = np.max(arr)
```

NumPy provides a wide range of functions for various mathematical operations, array manipulation, linear algebra, random number generation, and more. You can explore the official NumPy documentation for detailed information on all the available functions and their usage.

## Benefits of NumPy

- **Efficient array operations:** NumPy provides highly optimized functions for array operations, making it faster and more memory-efficient compared to traditional Python lists.
- **Multi-dimensional arrays:** NumPy allows you to work with multi-dimensional arrays, enabling efficient storage and manipulation of large datasets.
- **Mathematical functions:** NumPy includes a comprehensive collection of mathematical functions that can be applied to arrays, simplifying complex computations.
- **Integration with other libraries:** NumPy integrates well with other popular Python libraries such as Pandas, Matplotlib, and SciPy, providing a powerful ecosystem for scientific computing and data analysis.

NumPy is a fundamental library in the Python scientific computing ecosystem, and its versatility and performance make it an essential tool for any data scientist or researcher working with numerical data.

## Install Numpy with Types

```bash
%pip install nptyping beartype
```

`nptyping` and `beartype` are used for static typing in python code.

### To upgrade for latest versions

```bash
%pip install nptyping beartype --upgrade --force
```

This will upgrade the `beartype` and `nptyping` forcefully.

### Topics Covered

- simple lists
- Numpy vectors and Matrices
- Arrays with `nptyping` and `beartype`
- Arrays operations, finding maximum, mean, minimum, length and number of elements
- Array operations, Boolean search, arithmetic operations
- Numpy list operations
- Numpy 1D list operations
- Numpy 2D list operations
- Numpy Multi-dimensional list operations
- Numpy Random numbers
- intersection and where functions

## Numpy topics

## Numpy

**Numpy** stands for **Numerical Python**. It is extensivly used in machine learning projects. The most common way to work with numbers in numpy is through `ndarray` objects.

Some key concepts of numpy are

1. Scalars
2. Vectors
3. Matrices
4. Tensors

### Scalars

These types are important because every object we make (Vectors, Matrices, Tensors) eventually stores scalars. And when we create a numpy array, we can specify the type - but every item in the array must have the same type. In this regard numpy arrays are more like C arrays than Python **lists**.

```py
scalar = np.array(10)
```

### Vectors

Vectors in numpy have a single dimension, represented by a single row or column of elements. All elements in a vector are of same data type, such as integer, floats or complex numbers.

```py
vecor = np.array([1,2,3,4,5])
```

### Matrices

Matrices can be created using the `np.array` function. However, instead of just passing a list, we need to supply a list of lists where each list represents a row.

```py
array : np.ndarray = np.array(
    [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
```

### Tensors

Tensors are just like vectors and matrices, but they can have more dimensions. For example, to create 3*3*2*1, we could do the following:

```py
tensor = np.array(
    [[[1], [2]], [[3],[4]],[[5], [6]]],\
    [[[7], [8]], [[9],[10]],[[11], [12]]],\
    [[[13], [14]], [[15],[16]],[[17], [18]]]
)
```

**Numpy 101** exercise. <https://www.machinelearningplus.com/python/101-numpy-exercises-python/>
