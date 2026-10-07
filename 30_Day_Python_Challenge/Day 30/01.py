# Q1. Capstone: Build a simple `Library Management System` with classes `Book` and `Library`
# supporting add_book, borrow_book, return_book, and list_available_books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def __repr__(self):
        return f"{self.title} by {self.author}"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed: {book}")
                return
        print("Book not available")
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned: {book}")
                return
        print("This book was not borrowed")
    def list_available_books(self):
        available = [b for b in self.books if not b.is_borrowed]
        for b in available:
            print(b)
lib = Library()
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Dune", "Frank Herbert"))
lib.borrow_book("1984")
lib.list_available_books()
lib.return_book("1984")
lib.list_available_books()