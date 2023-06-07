from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horse_races = list()
        self.jockeys = list()
        self.horses = list()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse_mapper = \
            {
                "Appaloosa": Appaloosa,
                "Thoroughbred": Thoroughbred
            }

        if horse_type not in horse_mapper:
            return

        curr_type = horse_mapper[horse_type]

        self.__does_horse_exist(horse_name)

        curr_horse = curr_type(horse_name, horse_speed)
        self.horses.append(curr_horse)
        return f"{horse_type} horse {horse_name} is added."


    def add_jockey(self, jockey_name: str, age: int):
        self.__does_jockey_exist(jockey_name)
        curr_jockey = Jockey(jockey_name, age)
        self.jockeys.append(curr_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        self.__does_race_type_exists(race_type)
        curr_race = HorseRace(race_type)
        self.horse_races.append(curr_race)
        return f"Race {race_type} is created."


    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        curr_jockey = self.__find_jockey_by_name(jockey_name)
        curr_horse = self.__check_if_horse_is_available(horse_type)

        if curr_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        curr_jockey.horse = curr_horse
        curr_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {curr_horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        curr_race = self.__find_race_by_type(race_type)
        curr_jockey = self.__find_jockey_by_name(jockey_name)

        if curr_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if curr_jockey in curr_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        curr_race.jockeys.append(curr_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        curr_race = self.__find_race_by_type(race_type)
        if len(curr_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner, horse = self.__find_the_winner(curr_race)

        return f"The winner of the {race_type} race, with a speed of {horse.speed}km/h is {winner.name}! Winner's horse: {horse.name}."

    def __does_horse_exist(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

    def __does_jockey_exist(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

    def __does_race_type_exists(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def __check_if_horse_is_available(self, horse_type):
        horses = reversed(self.horses)
        for horse in horses:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        raise Exception(f"Race {race_type} could not be found!")

    def __find_the_winner(self, race):
        jockeys = race.jockeys
        fastest = jockeys[0]
        for jockey in jockeys:
            if jockey.horse.speed > fastest.horse.speed:
                fastest = jockey

        return fastest, fastest.horse
