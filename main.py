import random
options = ["rock", "paper", "scissors"]
def checkInput(usrInput):
    if choice == usrInput:
        print("pc picked: " + options[choice - 1])
        print("DRAW")
    elif usrInput - choice == -2:
        print("pc picked: " + options[choice - 1])
        print("you win!")
    elif usrInput - choice == 1:
        print("pc picked: " + options[choice - 1])
        print("you win!")
    elif usrInput > 3:
        print("PICK A NUMBER BETWEEN 1 AND 3!")
    else:
        print("pc picked: " + options[choice - 1])
        print("you lose!")
while (True):
    choice = random.randint(1, 3)
    usrInput = int(input("|CHOOSE: 1 = ROCK, 2 = PAPER, 3 = SCISSORS| "))
    checkInput(usrInput)
