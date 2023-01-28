from player import Player

import random
from time import sleep

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ['Rock','Paper','Scissors','Iron Fist','Nuke']
        sleep(1)
        print(f'{self.name} has chosen {gesture_list[int(self.choose_gesture)]}!')