from OOP.testing.testing_exercise.projects_to_test.project_mammal import Meal


class Starter(Meal):
    def __init__(self, name, price, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
