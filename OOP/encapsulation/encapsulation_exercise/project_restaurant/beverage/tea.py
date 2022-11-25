from OOP.encapsulation.encapsulation_exercise.project_restaurant.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)