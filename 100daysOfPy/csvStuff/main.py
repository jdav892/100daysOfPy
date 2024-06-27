#with open(f"C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/csvStuff/weather_data.csv") as day_values:
#    data = day_values.readlines()
#    print(data)

#import csv
#with open(f"C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/csvStuff/weather_data.csv") as day_values:
#    data = csv.reader(day_values)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)
#        
import pandas

#data = pandas.read_csv("C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/csvStuff/weather_data.csv")


#data_dict = data.to_dict()

#temp_list = data["temp"].to_list()
#print(round(data["temp"].max()))
#print(data["condition"])
#print(data.condition)

#print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
#monday_c_to_f = (monday.temp) *(9/5) + 32
#print(monday_c_to_f)

#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#    
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")
data = pandas.read_csv("C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/csvStuff/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240626.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")