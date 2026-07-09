from library import Library
from file_handler import FileHandler


class LibraryManagementSystem:

    def __init__(self):

        self.library = Library()

        self.library.books = FileHandler.load_books()
        self.library.members = FileHandler.load_members()

    def show_menu(self):

        print("\n" + "=" * 50)
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Book")
        print("2. Add Member")
        print("3. View Books")
        print("4. View Members")
        print("5. Search Book")
        print("6. Search Member")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Save Data")
        print("0. Exit")

        print("=" * 50)

        return input("Enter your choice: ")
    def run(self):

        while True:

            choice = self.show_menu()

            if choice == "1":

                self.library.add_book()

            elif choice == "2":

                self.library.add_member()

            elif choice == "3":

                self.library.view_books()

            elif choice == "4":

                self.library.view_members()

            elif choice == "5":

                self.library.search_book()

            elif choice == "6":

                self.library.search_member()

            elif choice == "7":

                self.library.borrow_book()

            elif choice == "8":

                self.library.return_book()

            elif choice == "9":

                FileHandler.save_books(
                    self.library.books
                )

                FileHandler.save_members(
                    self.library.members
                )

                print("Data saved successfully!")

            elif choice == "0":

                FileHandler.save_books(
                    self.library.books
                )

                FileHandler.save_members(
                    self.library.members
                )

                print("\nThank you for using Library Management System!")
                break

            else:

                print("Invalid choice! Please try again.")
def main():

        system = LibraryManagementSystem()

        system.run()

if __name__ == "__main__":

    main()