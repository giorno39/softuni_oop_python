from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def weight_increasement(self):
        return 0.25

    @property
    def edible_foods(self):
        return ["Meat"]

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def weight_increasement(self):
        return 0.35

    @property
    def edible_foods(self):
        return ["Meat", "Seed", "Vegetable", "Fruit"]



