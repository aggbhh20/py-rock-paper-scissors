import random
options = ["rock", "paper", "scissors"] #defining our options
def checkInput(usrInput):
    if choice == usrInput:
        #in case of draw
        print("pc picked: " + options[choice - 1])
        print("DRAW")
    elif usrInput - choice == -2:
        #rock(1) beats scissors(3) so rock-scissors = -2
        print("pc picked: " + options[choice - 1])
        print("you win!")
    elif usrInput - choice == 1:
        #paper(2) beats rock(1) so paper - rock = 1, scissors(3) beats paper(2) so scissors - paper = 1
        print("pc picked: " + options[choice - 1])
        print("you win!")
    elif usrInput > 3:
        #if the player enters a number bigger than 3
        print("PICK A NUMBER BETWEEN 1 AND 3!")
    else:
        #if the player does not meet the conditions to win
        print("pc picked: " + options[choice - 1])
        print("you lose!")
while (True):
    choice = random.randint(1, 3)
    usrInput = int(input("|CHOOSE: 1 = ROCK, 2 = PAPER, 3 = SCISSORS| "))
    checkInput(usrInput)
