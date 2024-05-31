print("Hello how are you?")

total = float(input("What was the total bill? "))

percentage = int(input("How much would you like to tip? 10, 12, 15? "))

people = int(input("How many people to split the bill? "))

total_per_person = total / people + ((total * (percentage/100)) / people) 
rounded_total = "{:.2f}".format(total_per_person)
print(f"Each person should pay: ${rounded_total}")




 