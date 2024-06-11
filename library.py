class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found.")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Books found:")
            for book in found_books:
                print(book)
        else:
            print("No books found with that title.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)


# Example usage
library = Library()

# Adding books
library.add_book(Book("Gitanjali", "Rabindranath Tagore", "1234567890"))
library.add_book(Book("The Guide", "R.K.Narayan", "1234567891"))
library.add_book(Book("A Suitable Boy", "Vikram Seth", "1234567892"))

# Displaying books
library.display_books()

# Searching for a book by title
library.search_book_by_title("1984")

# Removing a book
library.remove_book("1234567891")

# Displaying books after removal
library.display_books()
