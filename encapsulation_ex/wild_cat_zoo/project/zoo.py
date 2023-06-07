from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_money_needed = sum([w.salary for w in self.workers])
        if total_money_needed <= self.__budget:
            self.__budget -= total_money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_needed = sum([a.money_for_care for a in self.animals])
        if total_money_needed <= self.__budget:
            self.__budget -= total_money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + "\n".join(lions) + "\n"

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(tigers) + "\n"

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetahs) + "\n"

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"

        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"

        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets) + "\n"

        return result.strip()

