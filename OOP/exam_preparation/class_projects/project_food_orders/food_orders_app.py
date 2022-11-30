
from copy import copy

from OOP.exam_preparation.class_projects.project_food_orders.client import Client
from OOP.exam_preparation.class_projects.project_food_orders.meals.dessert import Dessert
from OOP.exam_preparation.class_projects.project_food_orders.meals.main_dish import MainDish
from OOP.exam_preparation.class_projects.project_food_orders.meals.starter import Starter


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number):

        current_client = Client(client_phone_number)

        try:
            next(filter(lambda p: p.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")

        except StopIteration:
            self.clients_list.append(current_client)
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ == "Starter" \
                    or meal.__class__.__name__ == "MainDish" \
                    or meal.__class__.__name__ == "Dessert":
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = [x.details() for x in self.menu]

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number, **kwargs):
        self.show_menu()
        try:
            self.register_client(client_phone_number)

        except Exception:
            pass

        objects_to_add = []

        for key, value in kwargs.items():
            meal_names = [x.name for x in self.menu]
            if key not in meal_names:
                raise Exception(f"{key} is not on the menu!")

            current_object = list(filter(lambda o: o.name == key, self.menu))
            if value > current_object[0].quantity:
                raise Exception(f"Not enough quantity of {current_object[0].__class__.__name__}: "
                                f"{current_object[0].name}!")

            objects_to_add.append(copy(current_object[0]))

        current_customer = list(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        for object in objects_to_add:
            for customer_key, customer_value in kwargs.items():
                if object.name == customer_key:
                    object.quantity = customer_value
                    current_customer[0].shopping_cart.append(object)
                    current_customer[0].bill += object.price * customer_value

        for k, v in kwargs.items():
            for obj in self.menu:
                if obj.name == k:
                    obj.quantity -= v


        total_meals = [x.name for x in current_customer[0].shopping_cart]

        return f"Client {client_phone_number} successfully ordered {', '.join(total_meals)} for " \
               f"{current_customer[0].bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client_obj = list(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client_obj[0].shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client_obj[0].shopping_cart:
            for menu_meal in self.menu:
                if meal.name == menu_meal.name:
                    menu_meal.quantity += meal.quantity

        client_obj[0].shopping_cart = []
        client_obj[0].bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client_obj = list(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client_obj[0].shopping_cart:
            raise Exception("There are no ordered meals!")

        all_meals = len(client_obj[0].shopping_cart)
        bill_amount = client_obj[0].bill

        client_obj[0].shopping_cart = []
        client_obj[0].bill = 0.0

        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {bill_amount:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)