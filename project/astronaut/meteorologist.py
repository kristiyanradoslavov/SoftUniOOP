from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS_PER_BREATH = 15

    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.UNITS_PER_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount
