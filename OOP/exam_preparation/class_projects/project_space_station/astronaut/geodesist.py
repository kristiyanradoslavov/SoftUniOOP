from OOP.exam_preparation.class_projects.project_space_station.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    UNITS_PER_BREATH = 10

    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.UNITS_PER_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def __str__(self):
        backpack_info = ', '.join(self.backpack) if self.backpack else "none"

        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {backpack_info}"