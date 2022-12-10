from OOP.exam.test_project.project_test_toy_store.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_initialisation(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_if_add_toy_raises_exception_when_shelf_doesn_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Q", "ivan")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_add_toy_raises_exception_when_trying_to_add_existing_toy(self):
        self.store.toy_shelf["A"] = "ivan"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "ivan")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_if_trying_to_add_to_a_taken_shelf_raises_exception(self):
        self.store.toy_shelf["A"] = "ivan"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "gosho")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_if_add_toy_adds_correctly_to_the_dict(self):
        self.store.toy_shelf["A"] = "ivan"
        self.store.add_toy("B", "gosho")

        self.assertEqual("ivan", self.store.toy_shelf["A"])
        self.assertEqual("gosho", self.store.toy_shelf["B"])
        self.assertEqual({
            "A": "ivan",
            "B": "gosho",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_if_add_toy_returns_correct_result(self):
        actual_result = self.store.add_toy("B", "gosho")
        expected_result = "Toy:gosho placed successfully!"

        self.assertEqual(expected_result, actual_result)

    def test_if_non_existing_toy_raises_error_on_remove_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Q", "gosho")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_non_existing_toy_is_tried_to_be_removed(self):
        self.store.toy_shelf["A"] = "ivan"
        self.store.toy_shelf["B"] = "gosho"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "gosho")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_if_toy_is_successfully_removed(self):
        self.store.toy_shelf["A"] = "ivan"
        self.store.toy_shelf["B"] = "gosho"
        self.store.remove_toy("A", "ivan")

        self.assertEqual(None, self.store.toy_shelf["A"])
        self.assertEqual({
            "A": None,
            "B": "gosho",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_if_remove_toy_func_returns_correct_result(self):
        self.store.toy_shelf["A"] = "ivan"
        self.store.toy_shelf["B"] = "gosho"
        actual_result = self.store.remove_toy("A", "ivan")
        expected_result = "Remove toy:ivan successfully!"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
