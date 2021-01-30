import tkinter as tk
import random

overall_food_dict = {}

with open("list_of_countries_and_recipes.csv", 'r') as recipe_file:
    recipe_file.readline()
    lines = recipe_file.readlines()
    for line in lines:
        continent, country, recipe_name, recipe_link, veg = line.split(',')

        if continent not in overall_food_dict:
            overall_food_dict[continent]= {}

        if country not in overall_food_dict[continent]:
            overall_food_dict[continent][country]= {}

        recipe= {'link': recipe_link, "Vegetarian" : veg}

        overall_food_dict[continent][country][recipe_name]= recipe

#print(overall_food_dict['North America']['Cuba']["Cuban Sandwich"]['link'])

#print(random.choice(["q", "w", "r"]))

def get_random_recipe():
    ''' () -> (value1, value2, value3)
        Return a Tuple with three random values from the dictionary.
    '''
    random_continent = random.choice(list(overall_food_dict.keys()))
    random_country = random.choice(list(overall_food_dict[random_continent].keys()))
    random_continent = "North America"
    random_country = "Cuba"
    random_recipe = random.choice(list(overall_food_dict[random_continent][random_country].keys()))
    return random_continent, random_country, random_recipe

root = tk.Tk()
root.title("Geo-Foodie")
frame = tk.Frame(root)
frame.pack()


label = tk.Label(root, fg="dark green")
label.pack()


def write_slogan():
    continent_choice, country_choice, recipe_choice = get_random_recipe()
    link = overall_food_dict[continent_choice][country_choice][recipe_choice]['link']
    argh = continent_choice + " " + country_choice + " " + recipe_choice + " " + link
    # print(choice)
    label.config(text=argh)


tk.Button(frame, text="QUIT", fg="red", command=quit).pack(side=tk.LEFT)

slogan = tk.Button(frame, text="Generate Recipe", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()