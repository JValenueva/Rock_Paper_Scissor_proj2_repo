from player import Player

class Human(Player):
    def __init__(self,name) -> None:
        super().__init__(name)
        

    def choose_gesture(self):
        return super().choose_gesture()