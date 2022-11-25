import tkinter as tk
import os

pizza = tk.Tk()
pointer = tk.IntVar()

# ADVANCED CODE
def images_Advanced():
    images = []

    for item in os.listdir("gifs"):
        if item.endswith(".gif"):
            images.append(tk.PhotoImage(file=f"gifs/{item}"))

    return images

# Basic code
def images_Basic():
    animal = tk.PhotoImage(file="gifs/animal.gif")
    cat = tk.PhotoImage(file="gifs/cat.gif")
    giraffe = tk.PhotoImage(file="gifs/giraffe.gif")

    return [animal, cat, giraffe]

images = images_Basic()

def next():
    pointer.set((pointer.get() + 1) % 3)
    L1.config(image=images[pointer.get()])

L1 = tk.Label(pizza, image=images[pointer.get()])
L1.grid()
B1 = tk.Button(pizza, text="Press me", command=next)
B1.grid()

pizza.mainloop()
