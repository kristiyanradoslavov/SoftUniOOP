from OOP.solid.solid_lab.SRP.books import Book


class Library:
    def __init__(self):
        self.books = []

    def find_book(self, title):
        if title in self.books:
            return title.title

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
