country = input("Input Country ")

visits = int(input("Enter the amount of visits "))

lists_of_cities = str(input("Where to? "))




travel_log = [
    {"country": "France",
     "cities": ["Paris", "Lille", "Dijon"],
     "visits" : 12
     },
    {"country" :"Germany" ,
     "cities": ["Berlin", "Hamburg", "Stuttgart"],
     "vists" : 16
     },
    {"country": "Japan",
     "cities" : ["Tokyo", "Kyoto", "Osaka", "Shinjuku", "Shibuya"],
     "visits" : 21
     },
]

def add_new_country(name, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = name
    new_country["cities"] = cities_visited 
    new_country["visits"] = times_visited 
    travel_log.append(new_country)

add_new_country(country, lists_of_cities, visits)
print(travel_log)