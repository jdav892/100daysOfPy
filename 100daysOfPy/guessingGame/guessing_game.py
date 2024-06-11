import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty_check = str(input("Choose a difficulty. Type 'easy' or 'hard' "))


computer_guess = random.randint(1, 100)

def hard_game(computer_guess):
        attempts = 5
        while attempts > 0:
            user_guess = int(input("Make a guess: "))
            if user_guess > computer_guess:
                attempts -=1
                print("Too High.\nGuess again.")
                print(f"You have {attempts} attempts remaining")
               
            elif user_guess < computer_guess:
                attempts -=1
                print("Too Low\nGuess again.")
                print(f"You have {attempts} attempts remaining")
              
            else:
                print(f"You got it! the answer was {user_guess}")
                return
            if attempts == 0:
               print("You lose!")
def easy_game(computer_guess):
    attempts = 10
    while attempts > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > computer_guess:
            attempts -= 1
            print("Too High.\nGuess again.")
            print(f"You have {attempts} attempts remaining")
           
        elif user_guess < computer_guess:
            attempts -= 1
            print("Too Low\nGuess again.")
            print(f"You have {attempts} attempts remaining")
      
        else:
            print(f"You got it! the answer was {user_guess}")
            
        if attempts == 0:
            print("You lose!")
        
if difficulty_check == 'hard':
    hard_game(computer_guess)
else:
    easy_game(computer_guess)
        