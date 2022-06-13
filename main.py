#Rock, Paper, Scissors.
print("Rock, Paper, Scissors...")
print("""Rules of the Game:
1. You and the CPU pick between Rock, Paper and Scissors simultaneously.
2. Rock beats Scissors.
3. Paper beats Rock.
4. Scissors beats Paper
5. If a tie occurs, you keep playing until there is a winner.

*********INSTRUCTIONS***************
Enter R, P or S
R stands for Rock
P stands for Paper and
S stands for Scissors
Note: Anything else apart from R, P or S would not be accepted
""")
import random
def R_P_S():
    while True:
        choices = ["R", "P", "S"]

        CPU = random.choice(choices)
        if CPU == "R":
            CPU = "Rock"
        elif CPU == "P":
            CPU = "Paper"
        elif CPU == "S":
            CPU = "Scissors"

        player = None

        while player not in choices:
            player = input("Rock, Paper, Scissors...: ").upper()
            if player not in choices:
                print("You did not enter a valid option. Try again.")
            else:
                continue
        if player == "R":
            player = "Rock"
        elif player == "P":
            player = "Paper"
        elif player == "S":
            player = "Scissors"


        if player == CPU:
            print("Player (",player,") : CPU (",CPU,")")
            print("Tie!")
            R_P_S()
        elif player == "Rock":
            if CPU == "Paper":
                print("Player (",player,") : CPU (",CPU,")")
                print("You lose!")
            if CPU == "Scissors":
                print("Player (",player,") : CPU (",CPU,")")
                print("You Win!")
        elif player == "Scissors":
            if CPU == "Paper":
                print("Player (",player,") : CPU (",CPU,")")
                print("You Win!")
            if CPU == "Rock":
                print("Player (",player,") : CPU (",CPU,")")
                print("You lose!")
        elif player == "Paper":
            if CPU == "Rock":
                print("Player (",player,") : CPU (",CPU,")")
                print("You Win!")
            if CPU == "Scissors":
                print("Player (",player,") : CPU (",CPU,")")
                print("You lose!")

        t = 0
        while t == 0:
            def play_again():
                play_again = input("Do you want to play Again? Y/N: ").upper()
                try:
                    if play_again == "Y":
                        t = 1
                        R_P_S()
                    elif play_again =="N":
                        print("Goodbye")
                        t = 1
                        quit()
                except:
                    print("You did not enter a valid option")

            play_again()
R_P_S()
