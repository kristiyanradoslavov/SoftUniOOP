from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name, price, portion):
        self.name = name
        self.price = price
        self.portion = portion

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0 or str.isspace(value):
            raise ValueError("Name cannot be null or whitespace!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("Price cannot be less or equal to zero!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass