from OOP.testing.testing_exercise.projects_to_test.project_mammal import Client
from OOP.testing.testing_exercise.projects_to_test.project_mammal import Dessert
from OOP.testing.testing_exercise.projects_to_test.project_mammal import MainDish
from OOP.testing.testing_exercise.projects_to_test.project_mammal import Starter


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):

        current_client = Client(client_phone_number)

        try:
            phone = next(filter(lambda p: p.phone_number == current_client.phone_number, self.clients_list))
            raise Exception("The client has already been registered!")

        except StopIteration:
            self.clients_list.append(current_client)

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


    def add_meals_to_shopping_cart(self,client_phone_number, **kwargs):
        pass


starter = Starter("qica", 10)
main = MainDish("banica", 3)
main_2 = MainDish("sirene", 3)
main_3 = Dessert("pacha", 3)
main_4 = Dessert("ruska salata", 3)
kur = Client("0898958699")

food = FoodOrdersApp()
food.add_meals_to_menu(starter, main, main_2, main_3, main_4)
print(food.show_menu())