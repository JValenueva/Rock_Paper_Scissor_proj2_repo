class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures_list = ['Rock','Paper','Scissors','Lizard','Spock']
        self.chosen_gesture = ''
        pass

    def choose_gesture(self):
        
        the_choice = input('Choose your weapon of choice[0 - 4]: ')
        print(the_choice)
        
        if the_choice == "0":
            # hold onto chosen gesture at 0
            print(f"You've chosen {self.gestures_list[0]}!")

        if the_choice == "1":
            print(f"You've chosen {self.gestures_list[1]}!")

        if the_choice == "2":
            print(f"You've chosen {self.gestures_list[2]}!")

        if the_choice == "3":
            print(f"You've chosen {self.gestures_list[3]}!")

        if the_choice == "4":
            print(f"You've chosen {self.gestures_list[4]}!")

        else:
            print("Can't recognize, try typing it again")
            self.choose_gesture()

        pass