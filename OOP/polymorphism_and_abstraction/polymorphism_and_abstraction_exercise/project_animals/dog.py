from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_animals.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"
