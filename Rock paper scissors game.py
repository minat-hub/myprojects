import random
import os
import re

os.system('cls' if os.name == 'nt' else 'clear')
while 1 < 2:
    print("\n")
    print("Rock, Paper, Scissors -Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter: ")
        print("[R]ock, [S]cissors or [P]aper.")
        continue
    # Echo the user's choice
    print("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)
    print("I chose: " + opponentChoice)
    if opponentChoice == str.upper(userChoice):
        print("Tie! ")
    # if opponentChoice == R and user choice == P
    elif opponentChoice == 'S' and userChoice.upper() == 'R':
        print("Scissors beats rock, I win! ")
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")
