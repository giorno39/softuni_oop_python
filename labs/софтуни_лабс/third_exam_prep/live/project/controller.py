from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = list()
        self.drivers = list()
        self.races = list()

    def create_car(self, car_type, model, speed_limit):
        car_dict = \
            {
                "MuscleCar": MuscleCar,
                "SportsCar": SportsCar
            }
        if car_type not in car_dict:
            return

        curr_type = car_dict[car_type]
        curr_car = curr_type(model, speed_limit)
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        self.cars.append(curr_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        curr_driver = Driver(driver_name)
        self.drivers.append(curr_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        curr_race = Race(race_name)
        self.races.append(curr_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__check_if_driver_exists(driver_name)
        car = self.__check_if_car_is_available(car_type)

        if driver.car is not None:
            driver.car.is_taken = False
            old_model = driver.car.model
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."



    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__check_if_race_exists(race_name)
        driver = self.__check_if_driver_exists(driver_name)

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__check_if_race_exists(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        result = ""
        for idx in range(3):
            curr_driver = winners[idx]
            curr_driver.number_of_wins += 1
            result += f"Driver {curr_driver.name} wins the {race_name} race with a speed of {curr_driver.car.speed_limit}."
            result += "\n"

        result = result.strip()
        return result

    def __check_if_driver_exists(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def __check_if_car_is_available(self, car_type):
        to_be_checked = reversed(self.cars)
        for car in to_be_checked:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def __check_if_race_exists(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")