from abc import ABC, abstractmethod


class Meal(ABC):

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            raise ValueError("Name cannot be an empty string!")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("Invalid price!")
        else:
            self.__price = value

    @abstractmethod
    def details(self):
        pass