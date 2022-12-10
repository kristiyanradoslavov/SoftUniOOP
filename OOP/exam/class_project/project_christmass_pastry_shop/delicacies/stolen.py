from OOP.exam.class_project.project_christmass_pastry_shop.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name, price, portion=250):
        super().__init__(name, price, portion)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
