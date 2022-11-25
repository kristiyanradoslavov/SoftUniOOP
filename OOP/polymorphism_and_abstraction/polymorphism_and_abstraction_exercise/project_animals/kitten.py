from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_animals.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, gender=Kitten.GENDER)

    def make_sound(self):
        return "Meow"

