from project.animals.animal import Mammal


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "Woof!"

    @property
    def weight_increasement(self):
        return 0.4

    @property
    def edible_foods(self):
        return ["Meat"]


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "Squeak"

    @property
    def weight_increasement(self):
        return 0.1

    @property
    def edible_foods(self):
        return ["Fruit", "Vegetable"]

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "Meow"

    @property
    def weight_increasement(self):
        return 0.3

    @property
    def edible_foods(self):
        return ["Meat", "Vegetable"]

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "ROAR!!!"

    @property
    def weight_increasement(self):
        return 1

    @property
    def edible_foods(self):
        return ["Meat"]
