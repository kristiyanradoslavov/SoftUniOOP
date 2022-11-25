from OOP.solid.solid_lab.OCP.animal import Animal


class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return "Meow Meow"