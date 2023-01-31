from ai import AI
from player import Player
from human import Human

class Game:
    def __init__(self) -> None:
        self.player_one = Human("Bob's Burgers")
        self.player_two = AI('Brother Bot 2.0')
        
        self.player = Player()
        pass
    
    def run_game(self):
        while self.player_one.score and self.player_two.score < 3:

            starter = input("How's about a game of rock, paper, scissor, iron fist, nuke aye?(y/n): ")
            print(starter)
            if starter == 'y':
                
                 print("Well alright then! Rules are simple.")
                 print(' ')
                 print('Scissors cuts paper')
                 print('Scissors decapitates lizard')
                 print('Paper disproves spock')
                 print('Paper covers rock')
                 print('Rock crushes scissors')
                 print('Rock crushes lizard')
                 print('Spock vaporizes rock')
                 print('Spock smashes scissors')
                 print('Lizard eats paper')
                 print('Lizard poisons spock')
                 print(' ')
                 print('Best out of three rounds walks away with victory in hand!')
                 print('Now! Begin!')
                
                 self.player_one.choose_gesture()
                 self.player_two.choose_gesture()
                 if self.player_one.chosen_gesture == self.player.gestures_list[0] and self.player_two.chosen_gesture == self.player.gestures_list[0]:
                    print('Tie go again!')

                 elif self.player_one.chosen_gesture == self.player.gestures_list[0] and self.player_two.chosen_gesture == self.player.gestures_list[1]:
                    print('Paper covers rock!')
                    self.add_point_ply2

                elif self.player_one.chosen_gesture == self.player.gestures_list[0] and self.player_two.chosen_gesture == self.player.gestures_list[2]:
                    print('Rock cushes scissors!')
                    self.add_point_ply1
                
                elif self.player_one.chosen_gesture == self.player.gestures_list[0] and self.player_two == self.player.gestures_list[3]:
                    print('Rock crushes lizard!')
                    self.add_point_ply1
                
                elif self.player_one.chosen_gesture == self.player.gestures_list[0] and self.player_two == self.player.gestures_list[4]:
                    print('Spock vaporizes rock!')
                    self.add_point_ply2

                    if self.player_two.score > 3:
                        print(f'{self.player_two.name} has defeated the player in a battle of wits and is declared the victor!')                        
                        break

                    elif self.player_one.score > 3:
                        print(f'The player has outdone {self.player_one.name} and taken the spectators by storm with a solid victory!')
                        break

            elif starter == 'n':
                 print("Well you're no fun, mate. Well I'll be off then.")
                 self.run_game()
        pass

    def add_point_ply1(self):
        self.player_one.score += 1
        
    def add_point_ply2(self):
        self.player_two.score += 1
        
    
