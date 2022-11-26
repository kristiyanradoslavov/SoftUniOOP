from unittest import TestCase, main

from OOP.testing.testing_exercise.projects_to_test.project_mammal.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Bear", "predator", "Roar")

    def test_initializing(self):
        self.assertEqual("Bear", self.mammal.name)
        self.assertEqual("predator", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        self.assertEqual("  ", self.mammal._Mammal__kingdom)

    def test_if_animal_func_returns_sound(self):
        self.assertEqual("Bear makes Roar", self.mammal.make_sound())

    def test_if_getter_returns_the_protected_attribute(self):
        self.assertEqual(self.mammal._Mammal__kingdom, self.mammal.get_kingdom())

    def test_if_func_info_returns_the_required_info(self):
        self.assertEqual("Bear is of type predator", self.mammal.info())


if "__main__" == __name__:
    main()
