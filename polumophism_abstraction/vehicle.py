from abc import ABC, abstractmethod


class Vehicle(ABC):
    AIR_CONDITIONER_CONSUMPTION = 0

    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)

