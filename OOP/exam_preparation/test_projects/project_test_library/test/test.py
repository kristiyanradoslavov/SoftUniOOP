from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("test1")
        self.library.books_by_authors = {"author1": ["book1", "book2"], "author2": []}
        self.library.readers = {"reader1": []}
        self.library2 = Library("test2")

    def test_initialisation(self):
        self.assertEqual("test2", self.library2.name)
        self.assertEqual({}, self.library2.books_by_authors)
        self.assertEqual({}, self.library2.readers)

    def test_if_name_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_if_new_author_is_created(self):
        self.library.add_book("author3", "book1")
        self.assertEqual({"author1": ["book1", "book2"], "author2": [], "author3": ["book1"]},
                         self.library.books_by_authors)

    def test_if_new_book_is_added_to_existing_author(self):
        self.library.add_book("author1", "book3")
        self.assertEqual({"author1": ["book1", "book2", "book3"], "author2": []}, self.library.books_by_authors)

    def test_if_new_author_is_added_to_an_empty_dict(self):
        self.library.books_by_authors = {}
        self.library.add_book("author1", "book1")
        self.assertEqual({"author1": ["book1"]}, self.library.books_by_authors)

    def test_if_new_reader_is_added_to_the_readers_dict(self):
        self.library.add_reader("reader2")
        self.assertEqual({"reader1": [], "reader2": []}, self.library.readers)

    def test_if_add_reader_returns_correct_result(self):
        actual_result = self.library.add_reader("reader1")
        expected_result = "reader1 is already registered in the test1 library."
        self.assertEqual(expected_result, actual_result)

    def test_non_existing_reader_return_result(self):
        actual_result = self.library.rent_book("reader6", "author1", "book1")
        expected_result = "reader6 is not registered in the test1 Library."
        self.assertEqual(expected_result, actual_result)

    def test_non_existing_book_author(self):
        actual_result = self.library.rent_book("reader1", "author19", "book1")
        expected_result = "test1 Library does not have any author19's books."
        self.assertEqual(expected_result, actual_result)

    def test_non_existing_book(self):
        actual_result = self.library.rent_book("reader1", "author1", "book19")
        expected_result = "test1 Library does not have author1's \"book19\"."
        self.assertEqual(expected_result, actual_result)

    def test_if_book_is_rented_successfully(self):
        self.library.rent_book("reader1", "author1", "book1")
        self.assertEqual({"reader1": [{"author1": "book1"}]}, self.library.readers)
        self.assertEqual({"author1": ["book2"], "author2": []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
