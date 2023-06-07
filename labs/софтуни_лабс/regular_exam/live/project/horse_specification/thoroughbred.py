from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    BREED_MAX_SPEED = 140
    SPEED_INCREASEMENT = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.BREED_MAX_SPEED, self.speed + self.SPEED_INCREASEMENT)