from OOP.exam.class_project.project_christmass_pastry_shop.booths.open_booth import OpenBooth
from OOP.exam.class_project.project_christmass_pastry_shop.booths.private_booth import PrivateBooth
from OOP.exam.class_project.project_christmass_pastry_shop.delicacies.gingerbread import Gingerbread
from OOP.exam.class_project.project_christmass_pastry_shop.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = ["Gingerbread", "Stolen"]
    VALID_BOOTHS = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def delicacy_name_exists(self, name):
        all_delicacies_names = [d.name for d in self.delicacies]
        if name in all_delicacies_names:
            return True
        else:
            return False

    def booth_number_exists(self, booth_number):
        all_booth_numbers = [b.booth_number for b in self.booths]
        if booth_number in all_booth_numbers:
            return True
        else:
            return False

    def add_delicacy(self, type_delicacy, name, price):
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if self.delicacy_name_exists(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            new_delicacy = Gingerbread(name, price)
        else:
            new_delicacy = Stolen(name, price)

        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        if type_booth not in ChristmasPastryShopApp.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        if self.booth_number_exists(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            new_booth = OpenBooth(booth_number, capacity)
        else:
            new_booth = PrivateBooth(booth_number, capacity)

        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        for booth in self.booths:
            if booth.is_reserved is False and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):
        current_booth = [b for b in self.booths if b.booth_number == booth_number]
        current_delicacy = [d for d in self.delicacies if d.name == delicacy_name]

        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")
        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth[0].delicacy_orders.append(current_delicacy[0])
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        current_booth = [b for b in self.booths if b.booth_number == booth_number][0]
        total_bill = 0
        total_bill += current_booth.price_for_reservation

        for delicacy in current_booth.delicacy_orders:
            total_bill += delicacy.price

        self.income += total_bill
        current_booth.delicacy_orders = []
        current_booth.price_for_reservation = 0
        current_booth.is_reserved = False

        return f"Booth {booth_number}:\n" \
               f"Bill: {total_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
