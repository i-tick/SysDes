from Book import Book

class BookCollectionV2:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def create_iterator(self):
        return self.BookIterator(self.books)

    class BookIterator:
        def __init__(self, books):
            self.books = books
            self.position = 0

        def has_next(self):
            return self.position < len(self.books)

        def next(self):
            if not self.has_next():
                raise StopIteration
            book = self.books[self.position]
            self.position += 1
            return book
        

if __name__ == "__main__":
    book_collection = BookCollectionV2()
    book_collection.add_book(Book("C++ Book"))
    book_collection.add_book(Book("Java Book"))
    book_collection.add_book(Book("Python Book"))

    iterator = book_collection.create_iterator()
    while iterator.has_next():
        print(iterator.next())
    # Output: