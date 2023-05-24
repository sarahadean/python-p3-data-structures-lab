spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
#take a list and return a list of strings with the name of each spicy food
# for meal in spicy_foods:
#      print(meal['name'])
# get_names(spicy_foods)
# returned each name of food but not in a list 
# Green Curry
# Buffalo Wings
# Mapo Tofu

def get_names(spicy_foods):
    spicy_meals = []
 
    for meal in spicy_foods:
        spicy_meals.append(meal["name"])
    return spicy_meals
# print(get_names(spicy_foods))

# ---------------------------------
#takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    extra_spicy = []
    for meal in spicy_foods:
        if meal["heat_level"] > 5:
            extra_spicy.append(meal)
    return extra_spicy

# print(get_spiciest_foods(spicy_foods))

# ---------------------------------
# that takes a list of spicy_foods and output to the terminal each spicy food in the following format using print(): 
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
# people = [
# 	("Bob", 42, "Mechanic"),
# 	("James", 24, "Artist"),
# 	("Harry", 32, "Lecturer")
# ]

# for name, age, profession in people:
# 	print(f"Name: {name}, Age: {age}, Profession: {profession}")

def print_spicy_foods(spicy_foods):
    for meal in spicy_foods:
        print(f'{meal["name"]} ({meal["cuisine"]}) | Heat Level: {meal["heat_level"] * "🌶"}')

# print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for meal in spicy_foods:
        if cuisine == meal['cuisine']:
            return meal

# takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:

# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
def print_spiciest_foods(spicy_foods):
    for meal in spicy_foods:
        if meal["heat_level"] > 5:
            print(f'{meal["name"]} ({meal["cuisine"]}) | Heat Level: {meal["heat_level"] * "🌶"}')

# takes a list of spicy_foods and returns an integer representing the average heat level of all the spicy foods in the array. 
# Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.
def get_average_heat_level(spicy_foods):
    #return sum(meal[heat_level] for meal in spicy_foods) / len(spicy_foods)
    length = len(spicy_foods)
    #add all heat levels together
    heat_sum = []
    for meal in spicy_foods:
        heat_sum.append(meal["heat_level"])
    return sum(heat_sum)/length


# Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added.  
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.insert(3, spicy_food)
    return spicy_foods
