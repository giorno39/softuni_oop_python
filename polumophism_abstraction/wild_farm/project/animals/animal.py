from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def weight_increasement(self):
        pass

    @property
    @abstractmethod
    def edible_foods(self):
        pass

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in self.edible_foods:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += self.weight_increasement * food.quantity
        self.food_eaten += food.quantity



class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
