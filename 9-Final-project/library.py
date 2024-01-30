from typing import List, Optional
from book import Book
from user import User


class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_book(self, book: Book):
        """Add a book to the library."""
        self.books.append(book)

    def borrow_book(self, user: User, title: str):
        """Allow a user to borrow a book."""
        book = next((b for b in self.books if b.title == title and b.available), None)
        if book:
            book.borrow()
            user.borrow_book(book)
        else:
            print(f"Book '{title}' not available.")

    def return_book(self, user: User, title: str):
        """Allow a user to return a borrowed book."""
        book = next((b for b in user.borrowed_books if b.title == title), None)
        if book:
            book.return_book()
            user.return_book(book)
        else:
            print(f"Book '{title}' not found in user's borrowed books.")

    def display_books(self):
        """Display information about available books in the library."""
        print("\nAvailable Books:")
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

    def display_users(self):
        """Display information about registered users."""
        print("\nRegistered Users:")
        for user in self.users:
            print(f"User ID: {user.user_id}, Name: {user.name}")
