import tkinter as tk

import random

mylist = [
    "paint with Bob Ross",
    "picnic",
    "massage",
    "charcuterie board",
    "movie night",
    "blindfolded dinner",
]


root = tk.Tk()
root.title("Date Night")
frame = tk.Frame(root)
frame.pack()


label = tk.Label(root, fg="dark green")
label.pack()


def write_slogan():
    choice = random.choice(mylist)
    # print(choice)
    label.config(text=choice)


tk.Button(frame, text="QUIT", fg="red", command=quit).pack(side=tk.LEFT)

slogan = tk.Button(frame, text="Press me", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()