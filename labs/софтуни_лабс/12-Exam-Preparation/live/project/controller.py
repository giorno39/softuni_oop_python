from project.player import Player


class Controller:
    MAX_PLAYER_STAMINA = 100

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player in self.players:
                continue
            self.players.append(player)
            added_players.append(player.name)
        result = "Successfully added: " + ", ".join(added_players)
        return result

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name, self.players)
        if player is None:
            return
        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        idx, supply = self.__find_supply(sustenance_type, self.supplies)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        player.stamina = min(self.MAX_PLAYER_STAMINA, player.stamina + supply.energy)
        self.supplies.pop(idx)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.__find_player_by_name(first_player_name, self.players)
        second_player = self.__find_player_by_name(second_player_name, self.players)

        result = ""
        if first_player.stamina == 0:
            result += f"Player {first_player.name} does not have enough stamina." + "\n"

        if second_player.stamina == 0:
            result += f"Player {second_player.name} does not have enough stamina."

        if result:
            return result.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        second_player.stamina -= first_player.damage


        first_player.stamina -= second_player.damage

        if first_player.stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"


        winner_name = first_player.name if first_player.stamina > second_player.stamina else second_player.name
        return f"Winner: {winner_name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"
        for supply in self.supplies:
            result += supply.details() + "\n"
        return result.strip()

    @staticmethod
    def __find_player_by_name(name, collection):
        for element in collection:
            if element.name == name:
                return element

    @staticmethod
    def __find_supply(name, collection):
        for idx in range(len(collection) - 1, -1, -1):
            if collection[idx].__class__.__name__ == name:
                return idx, collection[idx]
        return -1, None


