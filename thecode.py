import tkinter as tk
import random

overall_food_dict = {}

with open("list_of_countries_and_recipes.csv", 'r') as recipe_file:
    recipe_file.readline()
    lines = recipe_file.readlines()
    for line in lines:
        continent, country, recipe_name, recipe_link = line.split(',')

        if continent not in overall_food_dict:
            overall_food_dict[continent]= {}

        if country not in overall_food_dict[continent]:
            overall_food_dict[continent][country]= {}

        overall_food_dict[continent][country][recipe_name]= recipe_link

#print(overall_food_dict['North America']['Cuba']["Cuban Sandwich"])

#choice_overall_dict = ""

root = tk.Tk()
root.title("Geo-Foodie")
frame = tk.Frame(root)
frame.pack()


label = tk.Label(root, fg="dark green")
label.pack()


def write_slogan():
    choice = random.choice()
    # print(choice)
    label.config(text=choice)


tk.Button(frame, text="QUIT", fg="red", command=quit).pack(side=tk.LEFT)

slogan = tk.Button(frame, text="Generate Recipe", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()