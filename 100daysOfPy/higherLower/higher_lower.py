from art import logo
from art import vs
from game_data import data
import random

#set a run state based on how many attempts the user has to initialize the game
#use random selection for the dictionaries and compare the key value pair of  followers to play the game
#print to console to get make sure proper data is being selected
#Make the selection of either celeb using A or B inputs
#print logos on game start with the game title above the initial celeb name and the vs. art in between both names
#record user score and display it through the game
#end game after 1 wrong answer and print and ending game message


random_acc_two = random.choice(data)


print(logo)

score = 0
game_state = True
while game_state == True:
    random_acc = random_acc_two
    random_acc_two = random.choice(data)       
    if random_acc == random_acc_two:
        random_acc_two = random.choice(data)
    print(f"Compare A: {random_acc["name"]}, a {random_acc["description"]}, from {random_acc["country"]}")
    print(vs)
    print(f"Against B: {random_acc_two["name"]}, a {random_acc_two["description"]}, from {random_acc_two["country"]}")
    user_response = str(input("Who has more followers? Type 'A' or 'B' "))
    if user_response == 'A' and random_acc["follower_count"] > random_acc_two["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}.")
       
    elif user_response == 'B' and random_acc["follower_count"] > random_acc_two["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}.")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_state = False
            

