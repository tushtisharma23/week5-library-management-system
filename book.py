from datetime import datetime


class Book:

    def __init__(self, title, author, isbn, year):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.borrow_date = None
        self.due_date = None

    def check_out(self, member_id, borrow_date, due_date):

        if self.available:

            self.available = False
            self.borrowed_by = member_id
            self.borrow_date = borrow_date
            self.due_date = due_date

            return True

        return False

    def return_book(self):

        self.available = True
        self.borrowed_by = None
        self.borrow_date = None
        self.due_date = None

    def to_dict(self):

        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):

        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["year"]
        )

        book.available = data["available"]
        book.borrowed_by = data["borrowed_by"]
        book.borrow_date = data["borrow_date"]
        book.due_date = data["due_date"]

        return book

    def __str__(self):

        status = "Available"

        if not self.available:
            status = "Borrowed"

        return (
            f"{self.title} | "
            f"{self.author} | "
            f"{self.isbn} | "
            f"{status}"
        )