from OOP.exam_preparation.class_projects.project.car.car import Car


class MuscleCar(Car):
    MIN_LIMIT = 250
    MAX_LIMIT = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)


