from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    UNITS_PER_BREATH = 10

    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.UNITS_PER_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount
