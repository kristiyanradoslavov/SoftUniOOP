from OOP.testing.testing_exercise.projects_to_test.project_mammal import Meal


class Dessert(Meal):
    def __init__(self, name, price, quantity=30):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"