from abc import ABC, abstractmethod


class BakedFood(ABC):
    def __init__(self, name, price, portion):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0 or str.isspace(value):
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = value

    @abstractmethod
    def __repr__(self):
        pass
