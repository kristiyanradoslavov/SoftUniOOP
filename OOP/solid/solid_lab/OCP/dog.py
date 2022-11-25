from OOP.solid.solid_lab.OCP.animal import Animal


class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return "Woof Woof"
