from OOP.exam_preparation.class_projects.project.car.car import Car


class SportsCar(Car):
    MIN_LIMIT = 400
    MAX_LIMIT = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)