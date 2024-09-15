"""
Python async await
"""

import time


def q():
    """Prints a joke with a delay."""
    print("Why can't programmers tell jokes?")
    time.sleep(3)
    print("Because they are sleeping.")


def a():
    """Prints a timing message."""
    print("Timing!")


def main():
    """Calls the q function."""
    q()


a()
main()
