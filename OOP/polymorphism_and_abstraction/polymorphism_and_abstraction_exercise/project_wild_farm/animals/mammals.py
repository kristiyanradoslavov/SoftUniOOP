from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_wild_farm.animals.animal import Mammal
from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_wild_farm.food import *


class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def eat_food(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def eat_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def eat_food(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def eat_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00

