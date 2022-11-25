from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONING_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_fuel_consumption = (self.fuel_consumption + Car.AIR_CONDITIONING_CONSUMPTION) * distance
        if total_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONING_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_fuel_consumption = (self.fuel_consumption + Truck.AIR_CONDITIONING_CONSUMPTION) * distance
        if total_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


truck = Truck(100, 18)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
