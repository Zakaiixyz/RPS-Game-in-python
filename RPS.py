import random

def Player() :
    plr: str | None = None
    while plr != 'p' and plr != 'P' and plr != 's' and plr != 'S' and plr != 'R' and plr != 'r' : 
        plr = input("please Pick R/r for Rock , P/p for Paper , S/s for Scissors : ")
    if (plr == 'p' || plr == 'P') : return "Paper"
    elif (plr == 's' || plr == 'S') : return "Scissors"
    elif (plr == 'r' || plr == 'R') : return "Rock"



print("Welcome to ROCK-PAPER-SCISSORS game -Python edition-")

name = input("What is the Player's name ? : ")




computer = random.randrange(1 , 4)
if computer == 1 :
    computer = 'r'
elif computer == 2 :
    computer = 'p'
elif computer == 3 :
    computer = 's'

print(f"Computer({computer}) vs {name}({player}) : ")
if (player == 'R' or player == 'r') and (computer == 'r') :
    print("DRAW")
elif (player == 'P' or player == 'p') and (computer == 'p') :
    print("DRAW")
elif (player == 'S' or player == 's') and (computer == 's') :
    print("DRAW")
elif ((player == 'R' or player == 'r') and (computer == 's')) or ((player == 'P' or player == 'p') and (computer == 'r')) or ((player == 'S' or player == 's') and (computer == 'p')) :
    print(f"{name} WINS!")
elif ((computer == 'r') and (player == 'S' or player == 's')) or ((computer == 'p') and (player == 'R' or player == 'r')) or ((computer == 's') and (player == 'P' or player == 'p')) :
    print("THE COMPUTER WINS!!")

print("THANK YOU FOR PLAYING!!")