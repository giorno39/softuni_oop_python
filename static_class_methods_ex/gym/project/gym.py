from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
        self.trainers = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def subscription_info(self, subscription_id: int):
        curr_sub = self.__find_by_id(self.subscriptions, subscription_id)
        trainer = self.__find_by_id(self.trainers, curr_sub.trainer_id)
        customer = self.__find_by_id(self.customers, curr_sub.customer_id)
        plan = self.__find_by_id(self.plans, curr_sub.exercise_id)
        equipment = self.__find_by_id(self.equipment, plan.equipment_id)

        result = "\n".join([repr(curr_sub), repr(customer), repr(trainer), repr(equipment), repr(plan)])
        return result

    def __find_by_id(self, instance, id):
        for element in instance:
            if element.id == id:
                return element
