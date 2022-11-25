from OOP.encapsulation.encapsulation_exercise.project_restaurant.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)