# Class decorator for logging
def logger(cls):
    original_add = cls.add_book

    def new_add(self, book):
        print("Adding book:", book.get_title())
        original_add(self, book)

    cls.add_book = new_add
    return cls


# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn})"


# Library class with iterator
@logger
class Library:

    def __init__(self):
        self.books = []
        self.index = 0

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for b in self.books:
            if b.get_isbn() == isbn:
                self.books.remove(b)
                print("Book removed")
                return
        print("Book not found")

    # Iterator protocol
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


# Creating objects
book1 = Book("Python Basics", "Guido", "ISBN123")
book2 = Book("Data Structures", "Mark", "ISBN456")

library = Library()

library.add_book(book1)
library.add_book(book2)

# Iterator demonstration
for b in library:
    print(b)

# Attribute functions
print(hasattr(book1, "_Book__title"))
print(getattr(book1, "_Book__title"))

setattr(book1, "_Book__title", "Advanced Python")
print(getattr(book1, "_Book__title"))

# Remove book
library.remove_book("ISBN123")

