from abc import ABC, abstractmethod

from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_wild_farm.food import Food


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def eat_food(self):
        pass

    @property
    @abstractmethod
    def gained_weight(self):
        pass

    def feed(self, food: Food):
        if food.__class__ not in self.eat_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.gained_weight * food.quantity


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)

        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)

        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


