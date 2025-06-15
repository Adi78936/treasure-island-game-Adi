def treasure_island_game():
    print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     "=.|                  |
|___________________|__"=._o"-._        "=.______________|___________________
          |                "=._o"=._      _"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; "=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .   ,  "-._"-._   ". '__|___________________
          |           |o"=._ , " ; .". ,  "-._"-._; ;              |
 _________|___________| ;-.o"=._; ."  '."\  . "-._ /_______________|_______
|                   | |o ;    "-.o"=._  ' " ,__.--o;   |
|___________________|_| ;     (#) -.o "=._.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      ".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')

    print("🏝️ Welcome to Treasure Island.")
    print("Your mission is to find the hidden treasure! 💰")

    choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").strip().lower()

    if choice1 == "left":
        choice2 = input("You've come to a river. Do you want to 'swim' or 'wait' for a boat? ").strip().lower()
        if choice2 == "wait":
            choice3 = input("You arrive at three colored doors: one red, one blue, and one yellow. Which one do you choose? ").strip().lower()
            if choice3 == "yellow":
                print("🎉 Congratulations! You found the treasure! YOU WIN! 🏆")
            elif choice3 == "red":
                print("🔥 The room is full of fire. You got burned. Game Over.")
            elif choice3 == "blue":
                print("🐊 You enter a room full of beasts. Game Over.")
            else:
                print("🚪That's not a valid door. Game Over.")
        else:
            print("🐟 You were attacked by a trout while swimming. Game Over.")
    else:
        print("🕳️ You fell into a hole. Game Over.")

# Loop for replay
while True:
    treasure_island_game()
    replay = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("👋 Thanks for playing. See you next time!")
        break
#.strip() is a string method that removes any leading and trailing whitespace (spaces, tabs, newlines) from a string.
#Without .strip(), " lef " will be treated as-is, and it won’t match "left" in your if conditions.