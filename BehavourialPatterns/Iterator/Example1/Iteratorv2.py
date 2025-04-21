# from sortedcontainers import SortedSet

from Book import Book

class BookCollection:
    def __init__(self):
        self.books = []
        self.books = sorted(self.books, key=lambda book: book.get_title())

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return iter(self.books)
    
if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.add_book(Book("C++ Book"))
    book_collection.add_book(Book("Java Book"))
    book_collection.add_book(Book("Python Book"))

    for book in book_collection:
        print(book)
