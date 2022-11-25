from unittest import TestCase, main
from OOP.testing.testing_exercise.projects_to_test.project_vehicle.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(5.5, 150.50)

    def test_initialization(self):
        self.assertEqual(5.5, self.vehicle.fuel)
        self.assertEqual(150.50, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)

        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_the_fuel_is_decreased_after_driving(self):
        kilometers = 3
        fuel_needed = kilometers * self.vehicle.fuel_consumption
        remaining_fuel = self.vehicle.fuel - fuel_needed

        self.vehicle.drive(kilometers)

        self.assertEqual(remaining_fuel, self.vehicle.fuel)

    def test_if_exception_is_raised_when_the_required_fuel_is_more_than_the_actual(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_the_fuel_is_increase_when_refiling(self):
        self.vehicle.fuel -= 0.5
        self.vehicle.refuel(0.5)
        self.assertEqual(5.5, self.vehicle.fuel)

    def test_if_exception_is_raised_when_refiling_with_more_than_the_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_the_str_method_is_reinitialized(self):
        result = str(self.vehicle)

        self.assertEqual(f"The vehicle has 150.5 horse power with 5.5 fuel left and 1.25 fuel consumption",
                         result)


if "__main__" == __name__:
    main()
