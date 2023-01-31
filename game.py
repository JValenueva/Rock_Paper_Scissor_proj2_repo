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
                print('Rock crushes scissors')
                print("Nuke vaporizes that whom holds the mantle of 'iron fist'")
                print('Iron fist destroys scissors')
                print('Scissors defuses nuke')
                print('Nuke erases paper from this plane of existence')
                print('Paper diables that whom habors the power of the iron fist with a flurry of paper cuts')
                print('Iron fist demolishes rock into splinters of stone')
                print(' ')
                print('Best out of three rounds walks away with victory in hand!')
                print('Now! Begin!')
                
                self.ai.choose_gesture()
                self.player.choose_gesture()
                list_2 = ['Rock','Paper','Scissors','Iron Fist','Nuke']

                if self.ai.score >= 2:
                    print(f'{self.ai.name} has defeated the player in a battle of wits and is declared the victor!')                        
                    break

                elif self.player.score >= 2:
                    print(f'The player has outdone {self.ai.name} and taken the spectators by storm with a solid victory!')
                    break

            elif starter == 'n':
                print("Well you're no fun, mate. Well I'll be off then.")
                self.run_game()

    def add_point(self):
        self.ai.score += 1
        self.player.score += 1

    

uniR_1 = 'Rock' > 'Scissors' == True
uniR_2 = 'Rock' < 'Paper' == True
uniR_3 = 'Rock' < 'Nuke' == True
uniR_4 = 'Rock' < 'Iron fist' == True
uniR_5 = 'Paper' > 'Rock' == True
uniR_6 = 'Paper' < 'Scissors' == True
uniR_7 = 'Paper' < 'Nuke' == True
uniR_8 = 'Paper' > 'Iron fist' == True
uniR_9 = 'Scissors' > 'Paper' == True
uniR_10 = 'Scissors' < 'Rock' == True
uniR_11 = 'Scissors' > 'Nuke' == True
uniR_12 = 'Scissors' < 'Iron fist' == True
uniR_13 = 'Nuke' > 'Paper' == True
uniR_14 = 'Nuke' > 'Iron fist' == True
uniR_15 = 'Iron fist' > 'Scissors' == True
uniR_16 = 'Iron fist' > 'Rock' == True
