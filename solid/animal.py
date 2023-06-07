import abc


class Animal(abc.ABC):
    def __init__(self, species, sound="unknown sound"):
        self.species = species
        self.sound = sound

    def get_species(self):
        return self.species

    def make_sound(self):
        return self.sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Animal('cat', 'meow'), Animal('dog', 'woof-woof'), Animal('chicken')]


## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)
