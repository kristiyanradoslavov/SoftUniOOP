from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people):
        pass

    @abstractmethod
    def order_food(self, baked_food):
        pass

    @abstractmethod
    def order_drink(self, drink):
        pass

    @abstractmethod
    def get_bill(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def free_table_info(self):
        pass
