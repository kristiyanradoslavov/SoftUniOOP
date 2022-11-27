from unittest import TestCase, main

from OOP.testing.testing_lab.projects_to_test.car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("BMW", "M3", 10, 100)

    def test_initializing(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M3", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_empty_str_on_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_model_setter_raises_exception_when_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_fuel_consumption_raises_exception_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_capacity_raises_exception_when_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_setter_raises_exception_when_less_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_if_refuel_func_raises_exception_when_less_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_func_increases_fuel_amount_when_not_exceeding_the_capacity(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refuel_func_increases_fuel_amount_when_the_capacity_is_increased(self):
        self.car.refuel(150)
        self.assertEqual(100, self.car.fuel_amount)

    def test_if_drive_func_raises_exception_when_the_needed_fuel_is_more_than_the_actual(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_if_fuel_amount_is_decreased_on_drive_func(self):
        self.car.fuel_amount = 50
        needed_amount = (5 / 100) * self.car.fuel_consumption
        expected = self.car.fuel_amount - needed_amount

        self.car.drive(5)
        self.assertEqual(self.car.fuel_amount, expected)


if __name__ == '__main__':
    main()
