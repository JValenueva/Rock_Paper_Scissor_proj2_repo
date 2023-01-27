class Game:
    def __init__(self) -> None:
        pass
    
    def run_game(self):
        starter = input("How's about a game of rock, paper, scissor, iron fist, nuke aye?(y/n): ")
        print(starter)
        if starter == 'y':
            print("Well alright then! Rules are simple.")
            
            print('Scissors cuts paper')
            print('Paper covers rock')
            print("Nuke vaporizes that whom holds the mantle of 'iron fist'")
            print('Iron fist destroys scissors')
            print('Scissors defuses nuke')
            print('Nuke erases paper from this plane of existence')
            print('Paper diables that whom habors the power of the iron fist with a flurry of paper cuts')
            print('Iron fist demolishes rock into splinters of stone')
            print('Rock crushes scissors')
            
            choice_1 = input('How many players we talking?(1 - 3): ')
            print(choice_1)
            if choice_1 == '1':
                print("")
                choice_2 = input("Single or multiplayer, lad?(s/m): ")
                print(choice_2)
                if choice_2 == 's':
                    print("You'll be squaring off against a robot.")
            elif choice_1 == '2':

            elif choice_1 == '3':

            else:
                print()
        elif starter == 'n':
            print("Well you're no fun, mate. Well I'll be off then.")
