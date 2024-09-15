"""
Pass and continue usage
"""

def example_pass():
    """
    Demonstrates the use of the `pass` keyword.
    
    The `pass` keyword is used as a placeholder for future code. 
    When the `pass` statement is executed, nothing happens, but 
    you avoid getting an error when empty code is not allowed.
    """
    for i in range(5):
        if i == 2:
            pass  # Placeholder for future code
        print(f"Current number (pass example): {i}")


def example_continue():
    """
    Demonstrates the use of the `continue` keyword.
    
    The `continue` keyword is used to skip the current iteration of a 
    loop and continue with the next iteration.
    """
    for i in range(5):
        if i == 2:
            continue  # Skip the rest of the code inside the loop for this iteration
        print(f"Current number (continue example): {i}")


if __name__ == "__main__":
    example_pass()
    example_continue()
