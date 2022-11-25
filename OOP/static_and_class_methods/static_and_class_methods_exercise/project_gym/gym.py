from OOP.static_and_class_methods.static_and_class_methods_exercise.project_gym.customer import Customer
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_gym.equipment import Equipment
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_gym.exercise_plan import ExercisePlan
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_gym.subscription import Subscription
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        final_result = []
        current_subscription = [x for x in self.subscriptions if x.id == subscription_id]
        if current_subscription:
            final_result.append(str(current_subscription[0]))

            current_customer = [c for c in self.customers if current_subscription[0].customer_id == c.id]
            current_trainer = [t for t in self.trainers if current_subscription[0].trainer_id == t.id]
            current_plan = [p for p in self.plans if current_subscription[0].exercise_id == p.id]

            if current_customer:
                final_result.append(str(current_customer[0]))
            if current_trainer:
                final_result.append(str(current_trainer[0]))
            if current_plan:
                current_equipment = [e for e in self.equipment if current_plan[0].equipment_id == e.id]
                final_result.append(str(current_equipment[0]))
                final_result.append(str(current_plan[0]))

        return '\n'.join(final_result)
