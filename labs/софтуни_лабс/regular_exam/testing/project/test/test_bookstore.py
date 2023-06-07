from unittest import TestCase

from project.bookstore import Bookstore

class TestBookStore(TestCase):

    def test__init__expect_correct_values(self):
        self.book_store = Bookstore(10)
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual(0, self.book_store.total_sold_books)
        self.assertEqual(dict(), self.book_store.availability_in_store_by_book_titles)

    def test__init_when_limit_is_negative_expect_raise(self):
        with self.assertRaises(ValueError) as err:
            self.book_store = Bookstore(-5)

        self.assertEqual(f"Books limit of {-5} is not valid", str(err.exception))
        self.assertIsNotNone(err)

    def test__init_when_limit_is_zero_expect_raise(self):
        with self.assertRaises(ValueError) as err:
            self.book_store = Bookstore(0)

        self.assertEqual(f"Books limit of {0} is not valid", str(err.exception))
        self.assertIsNotNone(err)

    def test__len__expect_sum_of_values_in_dict(self):
        self.book_store = Bookstore(10)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5, "Potter": 3}
        self.assertEqual(8, len(self.book_store))

    def test__receive_book_when_exceeding_limit(self):
        self.book_store = Bookstore(5)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 4}
        with self.assertRaises(Exception) as err:
            self.book_store.receive_book("Potter", 5)

        self.assertIsNotNone(err)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(err.exception))

    def test__receive_book_when_there_is_a_new_book(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5}
        actual_result = self.book_store.receive_book("Potter", 3)
        expected_result = f"{3} copies of {'Potter'} are available in the bookstore."

        self.assertEqual({"Harry": 5, "Potter": 3}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(expected_result, actual_result)

    def test__receive_book_happy_case(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5, "Potter": 3}
        actual_result = self.book_store.receive_book("Harry", 5)
        expected_result = f"{10} copies of {'Harry'} are available in the bookstore."
        self.assertEqual(expected_result, actual_result)

    def test__sell_book_when_book_is_not_existing_expect_raise(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5}
        with self.assertRaises(Exception) as err:
            self.book_store.sell_book("Potter", 3)

        self.assertIsNotNone(err)
        self.assertEqual(f"Book {'Potter'} doesn't exist!", str(err.exception))

    def test__sell_book_when_we_dont_have_enough_copies(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5}

        with self.assertRaises(Exception) as err:
            self.book_store.sell_book("Harry", 8)

        self.assertIsNotNone(err)
        self.assertEqual(f"{'Harry'} has not enough copies to sell. Left: {5}", str(err.exception))

    def test__sell_book_with_happy_case(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 10}
        actual_result = self.book_store.sell_book("Harry", 5)
        expected_result = f"Sold {5} copies of {'Harry'}"
        self.book_store.sell_book("Harry", 2)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(3, self.book_store.availability_in_store_by_book_titles["Harry"])
        self.assertEqual(7, self.book_store.total_sold_books)

    def test__sell_book_when_there_are_no_books_left(self):
        self.book_store = Bookstore(20)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5}
        self.book_store.sell_book("Harry", 5)
        self.assertEqual({"Harry": 0}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, len(self.book_store))

    def test__str__expect_correct_representation(self):
        self.book_store = Bookstore(10)
        self.book_store.availability_in_store_by_book_titles = {"Harry": 5, "Potter": 3}
        result = [f"Total sold books: {0}",
                  f'Current availability: {8}',
                  f" - {'Harry'}: {5} copies",
                  f" - {'Potter'}: {3} copies"]

        expected_result = "\n".join(result)
        actual_result = str(self.book_store)
        self.assertEqual(expected_result, actual_result)

    def test__len__when_there_are_no_books(self):
        self.book_store = Bookstore(10)
        self.assertEqual(0, len(self.book_store))
