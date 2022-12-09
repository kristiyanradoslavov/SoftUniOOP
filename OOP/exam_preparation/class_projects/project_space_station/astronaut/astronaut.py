from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0 or str.isspace(value):
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def increase_oxygen(self, amount):
        pass

    @abstractmethod
    def __str__(self):
        pass
