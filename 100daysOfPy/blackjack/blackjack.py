import random
from art import logo

def deal_card():
    """Returns a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates score and swaps ace value of 11 for 1 if score is over 21"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Loser, opponent has Blackjack"
    elif user_score == 0:
        return "Winner, you have Blackjack"
    elif user_score > 21:
        return "Loser, you went over"
    elif computer_score > 21:
        return "Winner, your opponent went over LOL"
    elif user_score > computer_score:
        return "You win"
    else: 
        return "You lose"
         
def play_game():   
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        """Deals a pair of cards to the user and computer."""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:   
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(user_cards, user_score)
        print(computer_cards[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            """Checking conditions for game state"""
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' for another cards, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand {user_cards}, final score {user_score}")
    print(f"Your opponents hand {computer_cards}, opponents score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? 'y' for yes 'n' for no ") == "y":
    """Prompt user to start game and initialize the game through play_game()"""
    play_game()

    