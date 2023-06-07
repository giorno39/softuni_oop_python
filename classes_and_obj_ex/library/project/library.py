from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # Users
        self.books_available = {}  # {author: [books]}
        self.rented_books = {}  # {username: {book_name: days_left}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):

