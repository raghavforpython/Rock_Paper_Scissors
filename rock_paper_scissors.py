""" Rock Paper Scissors
----------------------------------------
"""
import random
import re

while 1 < 2:
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    USERCHOICE = input("Choose your weapon [R]ock], [P]aper, or [S]cissors or [E]xit: ")
    if not re.match("[SsRrPpEe]", USERCHOICE):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper or [E]xit")
        continue
    # Echo the user's choice
    print(f"You chose: {USERCHOICE}")
    if USERCHOICE.upper() == "E":
        print("Exiting as per the input")
        break
    CHOICES = ['R', 'P', 'S']
    OPPONENTCHOICE = random.choice(CHOICES)
    print(f"I chose: {OPPONENTCHOICE}")
    if OPPONENTCHOICE == str.upper(USERCHOICE):
        print("Tie! ")
    elif OPPONENTCHOICE == 'R' and USERCHOICE.upper() == 'S':
        print("Rock beats scissors, I win! ")
        continue
    elif OPPONENTCHOICE == 'S' and USERCHOICE.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif OPPONENTCHOICE == 'P' and USERCHOICE.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")
