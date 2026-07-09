import json
from book import Book
from member import Member


class FileHandler:

    @staticmethod
    def save_books(books):

        data = {}

        for isbn, book in books.items():
            data[isbn] = book.to_dict()

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_books():

        books = {}

        try:

            with open("books.json", "r") as file:

                data = json.load(file)

                for isbn, book_data in data.items():

                    books[isbn] = Book.from_dict(book_data)

        except:

            pass

        return books

    @staticmethod
    def save_members(members):

        data = {}

        for member_id, member in members.items():
            data[member_id] = member.to_dict()

        with open("members.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_members():

        members = {}

        try:

            with open("members.json", "r") as file:

                data = json.load(file)

                for member_id, member_data in data.items():

                    members[member_id] = Member.from_dict(member_data)

        except:

            pass

        return members