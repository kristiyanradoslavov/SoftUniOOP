from OOP.testing.testing_exercise.projects_to_test.project_mammal import Meal


class MainDish(Meal):
    def __init__(self, name, price, quantity=50):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"