from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, age, money_for_care=45):
        super().__init__(name, gender, age, money_for_care)