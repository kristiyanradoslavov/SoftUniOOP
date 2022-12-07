from OOP.exam_preparation.class_projects.project_medieval_games import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plant = Plantation(100)

    def test_initializing(self):
        self.assertEqual(100, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_if_size_setter_with_wrong_value(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.size = -5

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_if_hiring_existing_worker_raises_exception(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_if_hiring_non_existing_worker_adds_and_returns(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho"]
        actual_result = self.plant.hire_worker("Stanimir")
        expected_result = "Stanimir successfully hired."

        self.assertEqual(["Ivan", "Pesho", "Gosho", "Stanimir"], self.plant.workers)
        self.assertEqual(expected_result, actual_result)

    def test_if_len_func_is_overriden_correctly(self):
        self.plant.plants = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka"], "Pesho": []}
        self.assertEqual(4, len(self.plant))

    def test_if_planting_raises_exception_when_worker_is_not_in_the_list(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho"]

        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Stanimir", "Temenujka")

        self.assertEqual("Worker with name Stanimir is not hired!", str(ve.exception))

    def test_if_adding_more_plants_than_the_size_raises_exception(self):
        self.plant.size = 4
        self.plant.workers = ["Ivan", "Pesho", "Gosho"]
        self.plant.plants = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka"], "Pesho": []}

        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Ivan", "palma")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_if_planing_func_returns_correct_result_when_worker_in_the_dict(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho"]
        self.plant.plants = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka"], "Pesho": []}
        actual_result = self.plant.planting("Gosho", "palma")
        expected_result = "Gosho planted palma."

        actual_dict = self.plant.plants
        expected_dict = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka", "palma"], "Pesho": []}

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_dict, actual_dict)

    def test_if_planing_func_returns_correct_result_when_worker_not_in_the_dict(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho", "Stanimir"]
        self.plant.plants = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka"], "Pesho": []}
        actual_result = self.plant.planting("Stanimir", "palma")
        expected_result = "Stanimir planted it's first palma."

        actual_dict = self.plant.plants
        expected_dict = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka"], "Pesho": [],
                         "Stanimir": ["palma"]}

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_dict, actual_dict)

    def test_if_str_method_is_overriden_correctly(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho", "Stanimir"]
        self.plant.plants = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka", "no"], "Pesho": ["palma"]}

        actual_result = str(self.plant)
        expected_result = "Plantation size: 100\nIvan, Pesho, Gosho, Stanimir\n" \
                          "Ivan planted: Magnolia, Minzuhar, lale\nGosho planted: Temenujka, no\n" \
                          "Pesho planted: palma"

        self.assertEqual(expected_result, actual_result)

    def test_if_repr_method_is_overriden_correctly(self):
        self.plant.workers = ["Ivan", "Pesho", "Gosho", "Stanimir"]
        self.plant.plants = {"Ivan": ["Magnolia", "Minzuhar", "lale"], "Gosho": ["Temenujka", "no"], "Pesho": ["palma"]}

        actual_result = repr(self.plant)
        expected_result = "Size: 100\nWorkers: Ivan, Pesho, Gosho, Stanimir"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
