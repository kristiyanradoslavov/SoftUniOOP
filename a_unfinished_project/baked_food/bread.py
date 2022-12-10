from project_christmass_pastry_shop.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name, price, portion=200):
        super().__init__(name, price, portion)

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"


# bread = Bread("something", 100)
# print(bread.portion)
# print(bread)