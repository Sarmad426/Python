class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        """Mark the book as borrowed."""
        self.available = False

    def return_book(self):
        """Mark the book as returned."""
        self.available = True
