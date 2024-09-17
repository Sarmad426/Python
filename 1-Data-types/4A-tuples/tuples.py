"""
Python tuples
"""

from typing import Union

UserType = Union[tuple[str, str, int, bool]]


user: UserType = ("Sarmad", "sarmad@gmail.com", 19, True)

print(user)
