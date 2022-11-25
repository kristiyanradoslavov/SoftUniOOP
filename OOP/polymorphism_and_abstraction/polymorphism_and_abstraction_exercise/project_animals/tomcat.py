from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_animals.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, gender=Tomcat.GENDER)

    def make_sound(self):
        return "Hiss"
