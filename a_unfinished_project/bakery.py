class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.table_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0 or str.isspace(value):
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        pass

    def add_drink(self, drink_type, name, portion, brand):
        pass

    def add_table(self, table_type, table_number, capacity):
        pass

    def reserve_table(self, number_of_people):
        pass

    def order_food(self, table_number, *args):
        pass

    def order_drink(self, table_number, *args):
        pass

    def leave_table(self, table_number):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass
