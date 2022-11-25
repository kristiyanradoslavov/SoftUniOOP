from OOP.encapsulation.encapsulation_exercise.project_restaurant.food.starter import Starter


class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)
