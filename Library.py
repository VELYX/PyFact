class Book:
    def __init__(self, title, author):
        self.title = title    
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
 
    def remove_book(self, book):
        kept_books = []
        for b in self.books:
            if b.title != book.title or b.author != book.author:
                kept_books.append(b)
        self.books = kept_books

    def search_books(self, search_string):
        string_match = []
        for b in self.books:
            if search_string.casefold() in b.title.casefold() or search_string.casefold() in b.author.casefold():
                string_match.append(b)
        return string_match
