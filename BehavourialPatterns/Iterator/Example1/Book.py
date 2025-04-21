class Book:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return f"Book{{title='{self.title}'}}"

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return NotImplemented