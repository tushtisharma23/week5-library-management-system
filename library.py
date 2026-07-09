from book import Book
from member import Member


class Library:

    def __init__(self):

        self.books = {}
        self.members = {}

    def add_book(self):

        title = input("Book Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        year = input("Year: ")

        if isbn in self.books:

            print("Book already exists.")
            return

        self.books[isbn] = Book(
            title,
            author,
            isbn,
            year
        )

        print("Book added successfully!")

    def add_member(self):

        name = input("Member Name: ")
        member_id = input("Member ID: ")

        if member_id in self.members:

            print("Member already exists.")
            return

        self.members[member_id] = Member(
            name,
            member_id
        )

        print("Member added successfully!")

    def find_book(self, isbn):

        return self.books.get(isbn)

    def find_member(self, member_id):

        return self.members.get(member_id)
    def borrow_book(self):

        member_id = input("Member ID: ")
        isbn = input("Book ISBN: ")

        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member is None:
            print("Member not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if not book.available:
            print("Book is already borrowed.")
            return

        if member.borrow_book(isbn):

            book.check_out(member_id, "Today", "14 Days")
            print("Book borrowed successfully!")

        else:

            print("Borrow limit reached.")

    def return_book(self):

        member_id = input("Member ID: ")
        isbn = input("Book ISBN: ")

        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member is None or book is None:

            print("Invalid Member ID or ISBN.")
            return

        if member.return_book(isbn):

            book.return_book()
            print("Book returned successfully!")

        else:

            print("This member has not borrowed this book.")
    def view_books(self):

        if len(self.books) == 0:
            print("No books available.")
            return

        print("\n===== BOOK LIST =====")

        for book in self.books.values():
            print(book)

    def view_members(self):

        if len(self.members) == 0:
            print("No members available.")
            return

        print("\n===== MEMBER LIST =====")

        for member in self.members.values():
            print(member)

    def search_book(self):

        isbn = input("Enter ISBN: ")

        book = self.find_book(isbn)

        if book:
            print(book)
        else:
            print("Book not found.")

    def search_member(self):

        member_id = input("Enter Member ID: ")

        member = self.find_member(member_id)

        if member:
            print(member)
        else:
            print("Member not found.")