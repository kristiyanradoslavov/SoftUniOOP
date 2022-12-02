from abc import ABC, abstractmethod


class Horse(ABC):
    HORSE_MAX_SPEED = 0
    TRAIN_VALUE = 0

    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.HORSE_MAX_SPEED:
            raise ValueError("Horse speed is too high!")

        self.__speed = value

    def train(self):
        if self.__speed + self.TRAIN_VALUE <= self.HORSE_MAX_SPEED:
            self.__speed += self.TRAIN_VALUE

        else:
            self.__speed = self.HORSE_MAX_SPEED
