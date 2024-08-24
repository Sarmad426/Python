"""
    User class

    Manages the user
"""

from typing import List

from book import Book


class User:
    """
    User class

    Manages the user
    """

    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.borrowed_books: List[Book] = []

    def borrow_book(self, book: Book):
        """Add a borrowed book to the user's list."""
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        """Remove a returned book from the user's list."""
        self.borrowed_books.remove(book)
