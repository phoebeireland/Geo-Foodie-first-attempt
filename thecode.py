import tkinter as tk
import random

food_dictonary = {}

with open("list_of_countries_and_recipes.csv", 'r') as recipe_file:
    line = recipe_file.readline()
    print(line)

print(food_dictonary)


root = tk.Tk()
root.title("Geo-Foodie")
frame = tk.Frame(root)
frame.pack()


label = tk.Label(root, fg="dark green")
label.pack()


def write_slogan():
    choice = random.choice(food_dictonary)
    # print(choice)
    label.config(text=choice)


tk.Button(frame, text="QUIT", fg="red", command=quit).pack(side=tk.LEFT)

slogan = tk.Button(frame, text="Generate Recipe", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()