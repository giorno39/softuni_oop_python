import abc


class Book:
    def __init__(self, content: str):
        self.content = content

class Formatter(abc.ABC):
    @abc.abstractmethod
    def format(self, book: Book):
        return book.content


class FirstFormatter:
    def format(self, book: Book):
        return book.content


class SecondFormat:
    def format(self, book: Book):
        return book.content[2:]


class Printer(Formatter):

    def get_book(self, book: Book, formatter):
        to_be_printed = formatter.format(book)
        return to_be_printed



