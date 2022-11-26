from unittest import TestCase, main

from OOP.testing.testing_lab.projects_to_test.worker import Worker


class WorkerTest(TestCase):

    def setUp(self):
        self.worker = Worker("Ivan", 2000, 100)

    def test_initializing(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_the_energy_is_incremented_after_the_rest_method(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_if_exception_is_raised_when_worker_tries_to_work_with_zero_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_the_workers_money_are_increased_after_the_work_method_is_called(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_if_the_worker_energy_is_decreased_after_the_work_method_is_called(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_if_the_get_info_method_returns_correct_info(self):
        expected_result = self.worker.get_info()
        self.assertEqual("Ivan has saved 0 money.", expected_result)


if __name__ == "__main__":
    main()
