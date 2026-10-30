import random

print("Welcome to ROCK-PAPER-SCISSORS game -Python edition-")

name = input("What is the Player's name ? : ")
player: str | None = None

while player != 'p' and player != 'P' and player != 's' and player != 'S' and player != 'R' and player != 'r' : 
    player = input("please Pick R/r for Rock , P/p for Paper , S/s for Scissors : ")

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
