from OOP.exam_preparation.class_projects.project_horse_race.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_MAX_SPEED = 120
    TRAIN_VALUE = 2

    def __init__(self, name, speed):
        super().__init__(name, speed)


