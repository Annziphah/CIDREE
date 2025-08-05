"""
 4. OOP Design
 You are designing a library management system. Books can be borrowed and returned. Each book
 has a title, author, and availability status.
 Task: Design Python classes for this using OOP principles
"""

class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.available=True

    def borrow(self):
        if self.available:
            self.available = False
            print("Book Borrowed")
        else:
            print(" Not Available.")

    def return_book(self):
        self.available = True
        print("Book Returned")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added")

    def display_books(self):
        print("Available Books")
        for book in self.books:
            if book.available:
                status = "Available" 
            else:
                status="Borrowed"
            print("Title: {book.title}, Author: {book.author}, Status: {status}")
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print("Book '{title}' NOT FOUND.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print("Book '{title}' NOT FOUND.")


if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("Twilight", "Stepehnie"))
    lib.display_books()
    lib.borrow_book("Twilight")
    lib.return_book("Twilight")
        