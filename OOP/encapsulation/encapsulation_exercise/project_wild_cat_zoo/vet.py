from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
