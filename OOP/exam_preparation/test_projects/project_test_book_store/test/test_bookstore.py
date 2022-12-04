from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(100)

    def test_initializing(self):
        self.assertEqual(100, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_book_limit_setter_with_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_book_limit_setter_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            new_book = Bookstore(-5)

        self.assertEqual("Books limit of -5 is not valid", str(ve.exception))

    def test_if_len_func_is_overriden_correctly(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11, "book3": 20, "book4": 10}
        expected_result = len(self.store)

        self.assertEqual(45, expected_result)

    def test_if_receiving_more_books_than_the_limit_raises_an_error(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}
        self.store.books_limit = 16

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("book2", 2)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_if_receiving_more_books_adds_to_the_dict(self):  # have in mind, that I might need to test additionally
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}
        self.store.receive_book("book3", 5)
        self.store.receive_book("book4", 10)
        self.store.receive_book("book4", 10)

        expected_result = {"book1": 4, "book2": 11, "book3": 5, "book4": 20}

        self.assertEqual(expected_result, self.store.availability_in_store_by_book_titles)

    def test_if_receiving_a_book_which_is_already_in_the_store_updates_the_values(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}
        self.store.receive_book("book1", 4)

        self.assertEqual({"book1": 8, "book2": 11}, self.store.availability_in_store_by_book_titles)

    def test_if_receive_book_func_returns_correct_result(self):
        self.store.receive_book("book1", 4)
        self.store.receive_book("book2", 6)
        actual_result = self.store.receive_book("book2", 5)
        expected_result = "11 copies of book2 are available in the bookstore."
        self.assertEqual(expected_result, actual_result)

    def test_if_wrong_book_raises_exception_on_sell_book(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book3", 5)

        self.assertEqual("Book book3 doesn't exist!", str(ex.exception))

    def test_if_wrong_book_number_raises_exception_on_sell_book(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book1", 8)

        self.assertEqual("book1 has not enough copies to sell. Left: 4", str(ex.exception))

    def test_if_sell_book_func_can_sell_successfully(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}

        actual_return_result = self.store.sell_book("book1", 4)
        expected_return_result = "Sold 4 copies of book1"

        self.assertEqual(expected_return_result, actual_return_result)
        self.assertEqual({"book1": 0, "book2": 11}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(4, self.store.total_sold_books)

    def test_if_str_method_is_overriden_correctly(self):
        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 11}
        self.store._Bookstore__total_sold_books = 2

        expected_result = f"Total sold books: 2\nCurrent availability: 15\n - book1: 4 copies\n - book2: 11 copies"
        actual_result = str(self.store)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
