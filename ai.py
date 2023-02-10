from player import Player

import random
# from time import sleep

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        

    def choose_gesture(self):
        self.chosen_gesture = self.gestures_list[random.randint(0,4)]
        # sleep(1)
        print(f'{self.name} has chosen {self.chosen_gesture}!')
        