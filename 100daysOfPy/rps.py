import random

rando = random.randint(0, 2)

rock = 0 
paper = 1
scissors = 2
player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors "))
def rps(player, computer):
    if player == computer:
        print("It's a tie!")
    elif(player == rock and computer == scissors) or (player == paper and computer == rock) or (player == scissors and computer == paper):
        print("Player Wins")
    else:
        print("Computer Wins")
computer = rando
result = rps(player, computer)