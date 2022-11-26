from unittest import TestCase, main

from OOP.testing.testing_lab.projects_to_test.cat import Cat


class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Tom")

    def test_initializing(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_if_eat_func_raises_exception_if_trying_to_feed_when_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_if_params_are_changed_after_feeding(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_if_trying_to_sleep_when_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_if_sleeping_param_is_changed_when_cat_has_slept(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
