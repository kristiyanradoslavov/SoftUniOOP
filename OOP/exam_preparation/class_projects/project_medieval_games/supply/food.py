from OOP.exam_preparation.class_projects.project_medieval_games.supply.supply import Supply


class Food(Supply):
    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f"Food: {self.name}, {self.energy}"
