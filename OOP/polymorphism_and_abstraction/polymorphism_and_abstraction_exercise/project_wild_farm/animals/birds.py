from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_wild_farm.animals.animal import Bird
from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_wild_farm.food import *


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def eat_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def eat_food(self):
        return [Meat, Vegetable, Seed, Fruit]

    @property
    def gained_weight(self):
        return 0.35



