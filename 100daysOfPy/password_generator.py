import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numbers = ['1', '2', '3', '4', '5']
symbols = ['!', '@', '#', '$', '%'] 

print("Welcome to Password Generator")
letter_num = int(input("How many letters would you like? \n"))

number_num = int(input("How many numbers would you like? \n"))

symbol_num = int(input("How many symbols would you like? \n")) 

#password = ""
#
#for char in range(1, letter_num + 1):
#    password += random.choice(letters)
#
#for char in range(1, number_num + 1):
#    password += random.choice(numbers)
#
#for char in range(1, symbol_num + 1):
#    password += random.choice(symbols)
#
#print(password)

password = []

for char in range(1, letter_num + 1):
    password += random.choice(letters)

for char in range(1, number_num + 1):
    password += random.choice(numbers)

for char in range(1, symbol_num + 1):
    password += random.choice(symbols)

random.shuffle(password)
pass_word= ""
for char in password:
    pass_word += char

print(f"Your password is : {pass_word}")