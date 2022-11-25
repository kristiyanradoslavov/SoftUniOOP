from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.animal import Animal
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.caretaker import Caretaker
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.cheetah import Cheetah
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.keeper import Keeper
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.lion import Lion
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.tiger import Tiger
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.vet import Vet
from OOP.encapsulation.encapsulation_exercise.project_wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) + 1 <= self.__animal_capacity and self.__budget - price >= 0:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.animals) + 1 <= self.__animal_capacity and self.__budget - price < 0:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) + 1 > self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for current_worker in self.workers:
            total_salary += current_worker.salary

        if total_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_budget = 0
        for current_animal in self.animals:
            animal_budget += current_animal.money_for_care

        if animal_budget > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animal_budget
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        final_result = [f"You have {len(self.animals)} animals"]
        result_dict = {"Lion": 0, "Tiger": 0, "Cheetah": 0}
        for current_animal in self.animals:
            for current_key in result_dict.keys():
                if current_animal.__class__.__name__ == current_key:
                    result_dict[current_key] += 1

        final_result.append(f"----- {result_dict['Lion']} Lions:")
        for lions in self.animals:
            if lions.__class__.__name__ == "Lion":
                final_result.append(str(lions))

        final_result.append(f"----- {result_dict['Tiger']} Tigers:")
        for tigers in self.animals:
            if tigers.__class__.__name__ == "Tiger":
                final_result.append(str(tigers))

        final_result.append(f"----- {result_dict['Cheetah']} Cheetahs:")
        for cheetah in self.animals:
            if cheetah.__class__.__name__ == "Cheetah":
                final_result.append(str(cheetah))

        return "\n".join(final_result)

    def workers_status(self):
        final_result = [f"You have {len(self.workers)} workers"]
        workers_dict = {"Keeper": 0, "Caretaker": 0, "Vet": 0}
        for current_worker in self.workers:
            for current_key in workers_dict.keys():
                if current_key == current_worker.__class__.__name__:
                    workers_dict[current_key] += 1

        final_result.append(f"----- {workers_dict['Keeper']} Keepers:")
        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                final_result.append(str(w))

        final_result.append(f"----- {workers_dict['Caretaker']} Caretakers:")
        for k in self.workers:
            if k.__class__.__name__ == "Caretaker":
                final_result.append(str(k))

        final_result.append(f"----- {workers_dict['Vet']} Vets:")
        for v in self.workers:
            if v.__class__.__name__ == "Vet":
                final_result.append(str(v))

        return "\n".join(final_result)


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
