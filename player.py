class Player:
    def __init__(self):
        self.score = 0

    def choose_gesture(self):
        list_1 = ['Rock','Paper','Scissors','Iron Fist','Nuke']
        print(list_1)
        
        self.gesture_choice = input('Choose your weapon of choice: ')
        print(self.gesture_choice)
        
        if self.gesture_choice == list_1[0]:
            print(f"You've chosen {list_1[0]}!")

        if self.gesture_choice == list_1[1]:
            print(f"You've chosen {list_1[1]}!")

        if self.gesture_choice == list_1[2]:
            print(f"You've chosen {list_1[2]}!")

        if self.gesture_choice == list_1[3]:
            print(f"You've chosen {list_1[3]}!")

        if self.gesture_choice == list_1[4]:
            print(f"You've chosen {list_1[4]}!")

        else:
            print("Can't recognize, try typing it again")
            self.choose_gesture()
        