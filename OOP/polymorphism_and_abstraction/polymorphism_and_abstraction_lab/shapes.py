from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self._radius


class Rectangle(Shape):
    def __init__(self, height, width):
        super(Rectangle, self).__init__()

        self._height = height
        self._width = width

    def calculate_area(self):
        return self._height * self._width

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


