from OOP.exam_preparation.class_projects.project.car.muscle_car import MuscleCar
from OOP.exam_preparation.class_projects.project.car.sports_car import SportsCar
from OOP.exam_preparation.class_projects.project.driver import Driver
from OOP.exam_preparation.class_projects.project.race import Race


class Controller:
    VALID_CAR_TYPES = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def get_last_car_added(self, type):
        result = []
        for car in range(len(self.cars) -1, -1, -1):
            if self.cars[car].__class__.__name__ == type and self.cars[car].is_taken is False:
                result.append(self.cars[car])
                break

        if not result:
            raise Exception(f"Car {type} could not be found!")
        else:
            return result[0]

    def create_car(self, car_type, model, speed_limit):
        all_car_models = [m.model for m in self.cars]

        if car_type in Controller.VALID_CAR_TYPES:
            if model in all_car_models:
                raise Exception(f"Car {model} is already created!")

            if car_type == "MuscleCar":
                new_car = MuscleCar(model, speed_limit)
            else:
                new_car = SportsCar(model, speed_limit)

            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        all_driver_names = [d.name for d in self.drivers]
        if driver_name in all_driver_names:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        all_race_names = [r.name for r in self.races]
        if race_name in all_race_names:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver_instance = [d for d in self.drivers if d.name == driver_name]
        if not driver_instance:
            raise Exception(f"Driver {driver_name} could not be found!")

        car_instance = self.get_last_car_added(car_type)

        if driver_instance[0].car is not None:
            old_model = driver_instance[0].car.model
            driver_instance[0].car.is_taken = False
            driver_instance[0].car = car_instance
            driver_instance[0].car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {driver_instance[0].car.model}."
        else:
            driver_instance[0].car = car_instance
            driver_instance[0].car.is_taken = True
            return f"Driver {driver_name} chose the car {car_instance.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race_instance = [r for r in self.races if race_name == r.name]
        driver_instance = [d for d in self.drivers if driver_name == d.name]
        if not race_instance:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver_instance:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver_instance[0].car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race_drivers = [rd for rd in race_instance[0].drivers if driver_name == rd.name]

        if not race_drivers:
            race_instance[0].drivers.append(driver_instance[0])
            return f"Driver {driver_name} added in {race_name} race."
        else:
            return f"Driver {driver_name} is already added in {race_name} race."

    def start_race(self, race_name):
        race_instance = [r for r in self.races if race_name == r.name]
        if not race_instance:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race_instance[0].drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race_instance[0].drivers, key= lambda x: -x.car.speed_limit)

        winners = []
        for car in range(len(sorted_drivers)):
            sorted_drivers[car].number_of_wins += 1
            winners.append(sorted_drivers[car])
            if len(winners) == 3:
                break

        final_result = []
        for i in winners:
            final_result.append(f"Driver {i.name} wins the {race_name} race with a speed of {i.car.speed_limit}.")

        return '\n'.join(final_result)


