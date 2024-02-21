"""
Fibonacci Series python 
Example fibonacci series up to 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

from typing import List


def fibonacci(n: int) -> List[int]:
    """
    Generate Fibonacci series up to the nth term.

    Parameters:
        n (int): The number of terms in the Fibonacci series to generate.

    Returns:
        List[int]: A list containing the Fibonacci series up to the nth term.
    """
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]


N_TERMS = 10
FIB_SERIES = fibonacci(N_TERMS)
print(f"Fibonacci series up to {N_TERMS} terms:", FIB_SERIES)
