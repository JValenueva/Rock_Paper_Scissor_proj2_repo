from ai import AI
from player import Player
from human import Human

class Game:
    def __init__(self) -> None:
        self.ai = AI('Brother Bot 2.0')
        self.human = Human()
        self.player = Player()
    
    def run_game(self):
        while self.ai.score and self.player.score < 2:

            starter = input("How's about a game of rock, paper, scissor, iron fist, nuke aye?(y/n): ")
            print(starter)
            if starter == 'y':
                
                print("Well alright then! Rules are simple.")
                print(' ')
                print('Scissors cuts paper')
                print('Paper covers rock')
                print("Nuke vaporizes that whom holds the mantle of 'iron fist'")
                print('Iron fist destroys scissors')
                print('Scissors defuses nuke')
                print('Nuke erases paper from this plane of existence')
                print('Paper diables that whom habors the power of the iron fist with a flurry of paper cuts')
                print('Iron fist demolishes rock into splinters of stone')
                print('Rock crushes scissors')
                print(' ')
                print('Best out of three rounds walks away with victory in hand!')
                print('Now! Begin!')
                
                self.ai.choose_gesture()
                self.player.choose_gesture()
                list_2 = ['Rock','Paper','Scissors','Iron Fist','Nuke']
                if self.ai.choose_gesture() == list_2[0]:
                    
            
                    if self.ai.score >= 2:
                        print(f'{self.ai.name} has defeated the player in a battle of wits and is declared the victor!')
                        break

                    elif self.player.score >= 2:
                        print(f'The player has outdone {self.ai.name} and taken the spectators by storm with a solid victory!')
                        break

            elif starter == 'n':
                print("Well you're no fun, mate. Well I'll be off then.")
                self.run_game()