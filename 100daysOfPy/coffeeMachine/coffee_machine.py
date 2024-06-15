

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#buyer_request = str(input("What would you like? (espresso/latte/cappuccino): "))
#
#money_count = 0
#active = True
#
#def make_coffee(drink_name, resources, menu):
#    global money_count
#    
#    if buyer_request == "espresso" or buyer_request == "latte" or buyer_request == "cappuccino":
#        print("Please insert coins")
#        quarter_amount = (int(input("How many quarters? ")))
#        dime_amount = (int(input("How many dimes? ")))
#        nickel_amount = (int(input("How many nickels? ")))
#        penny_amount = (int(input("How many pennies? ")))
#        buyer_coin_amount = float((quarter_amount * .25) + (dime_amount * .10) + (nickel_amount * .05) + (penny_amount * .01))
#        change = buyer_coin_amount - MENU[drink_name]["cost"]
#        print(f"Here is ${change:.2f} in change.")
#    
#    if drink_name in MENU:
#        ingredients = MENU[drink_name]["ingredients"]
#        
#        for item in ingredients:
#            if item not in resources or resources[item] < ingredients[item]:
#                print(f"Sorry, there is not enough {item}")
#                return 
#        for item in ingredients:
#            if item in ingredients:
#                resources[item] -= ingredients[item]
#                
#            money_count += MENU[drink_name]["cost"]
#            print(f"Here is your {drink_name} enjoy")
#            return
#    elif drink_name == "report":
#        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money_count}")
#        return
#run = make_coffee(buyer_request, resources, MENU)

profit = 0

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            