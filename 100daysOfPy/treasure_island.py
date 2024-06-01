print("Welcome to Treasure Island. Your mission is to find the treasure")

direction = str(input("You're at a cross road where do you want to go? Left or Right? ").lower())





if direction == "left":
    swim_or_not = str(input("You come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across ").lower())
    if swim_or_not == "wait":
        door = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? ").lower())
        if door == "yellow": 
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else: 
    print("Game Over.")

    