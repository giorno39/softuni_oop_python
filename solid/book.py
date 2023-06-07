class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} from {self.author} is on {self.page} page"


class Library:
    def __init__(self, books):
        self.books = books


    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book


first = Book("Pod Igoto", "Ivan Vazov")
second = Book("Tiutiun", "Ne go pomna")
third = Book("Malkiq princ", "nqkoi si")

pz_biblioteka = Library([first, second, third])
my_book = pz_biblioteka.find_book("Pod Igoto")
print(my_book)
