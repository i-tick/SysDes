

from Book import Book

class BookCollectionV1:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books


if __name__ == "__main__":
    book_collection = BookCollectionV1()
    book_collection.add_book(Book("C++ Book"))
    book_collection.add_book(Book("Java Book"))
    book_collection.add_book(Book("Python Book"))

    for book in book_collection.get_books():
        print(book)