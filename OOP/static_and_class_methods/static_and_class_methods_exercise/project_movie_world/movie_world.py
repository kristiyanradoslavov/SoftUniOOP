from OOP.static_and_class_methods.static_and_class_methods_exercise.project_movie_world.customer import Customer
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        elif current_dvd.is_rented:
            return "DVD is already rented"

        elif current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        else:
            current_dvd.is_rented = True
            current_customer.rented_dvds.append(current_dvd)
            # self.dvds.remove(current_dvd)       # should I remove it from here ?
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            # self.dvds.append(current_dvd)
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        else:
            return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for current_customer in self.customers:
            result.append(str(current_customer))

        for current_dvd in self.dvds:
            result.append(str(current_dvd))

        return "\n".join(result)


