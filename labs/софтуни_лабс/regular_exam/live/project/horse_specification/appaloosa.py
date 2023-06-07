from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    BREED_MAX_SPEED = 120
    SPEED_INCREASEMENT = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.BREED_MAX_SPEED, self.speed + self.SPEED_INCREASEMENT)
