from library import Library
from book import Book
from user import User


def main():
    # Create a Library instance
    library = Library()

    # Add some sample books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
    book3 = Book("1984", "George Orwell", "978-0-452-28423-4")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Add a sample user
    user = User("123", "John Doe")

    # User borrows a book
    library.borrow_book(user, "The Great Gatsby")

    # Display library information
    library.display_books()
    library.display_users()


if __name__ == "__main__":
    main()
