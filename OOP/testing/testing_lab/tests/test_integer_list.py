from unittest import TestCase, main

# from OOP.testing.testing_lab.projects_to_test.integer_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integers_list = IntegerList(1, 2, 3, 4, 5, 6)

    def test_initializing(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], self.integers_list._IntegerList__data)

    def test_of_getter_returns_correct_info(self):
        expected_result = self.integers_list.get_data()
        self.assertEqual(expected_result, self.integers_list._IntegerList__data)

    def test_if_add_raises_error_when_trying_to_add_non_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.integers_list.add("banica")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_if_element_is_appended_to_the_list(self):
        self.integers_list.add(7)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], self.integers_list._IntegerList__data)

    def test_if_add_func_returns_correct_info(self):
        expected_result = self.integers_list.add(7)

        self.assertEqual(self.integers_list._IntegerList__data, expected_result)

    def test_if_wrong_index_raises_Index_error_on_remove_index_func(self):
        with self.assertRaises(IndexError) as ie:
            self.integers_list.remove_index(6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_if_element_is_deleted_when_calling_remove_index(self):
        self.integers_list.remove_index(0)
        self.assertEqual([2, 3, 4, 5, 6], self.integers_list._IntegerList__data)

    def test_if_remove_index_func_returns_the_removed_num(self):
        expected_result = self.integers_list.remove_index(0)
        self.assertEqual(1, expected_result)

    def test_if_get_func_raises_Index_error_when_receiving_wrong_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integers_list.get(6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_if_get_func_returns_correct_data(self):
        expected_result = self.integers_list.get(0)
        self.assertEqual(1, expected_result)

    def test_if_insert_func_raises_index_error_when_receiving_wrong_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integers_list.insert(6, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_if_insert_func_raises_value_error_when_receiving_non_integer_number(self):
        with self.assertRaises(ValueError) as ve:
            self.integers_list.insert(3, "banica")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_if_insert_func_inserts_element_in_the_list(self):
        self.integers_list.insert(5, 7)
        self.assertEqual([1, 2, 3, 4, 5, 7, 6], self.integers_list._IntegerList__data)

    def test_if_get_biggest_func_returns_correct_result(self):
        self.assertEqual(6, self.integers_list.get_biggest())

    def test_if_get_index_func_returns_correct_info(self):
        expected_result = self.integers_list.get_index(1)
        self.assertEqual(0, expected_result)


if __name__ == "__main__":
    main()
