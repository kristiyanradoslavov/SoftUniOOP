from OOP.exam_preparation.class_projects.project_horse_race.horse_specification.horse import Horse


class Thoroughbred(Horse):
    HORSE_MAX_SPEED = 140
    TRAIN_VALUE = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

