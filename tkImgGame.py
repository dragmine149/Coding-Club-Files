import tkinter as tk

# define object
dave = tk.Tk()

def wrong():
    L1.config(image=cat)

def correct():
    L1.config(image=giraffe)

# define images
animal = tk.PhotoImage(file="gifs/animal.gif")
cat = tk.PhotoImage(file="gifs/cat.gif")
giraffe = tk.PhotoImage(file="gifs/giraffe.gif")

# define labels and buttons
L1 = tk.Label(dave, image=animal)
B1 = tk.Button(dave, text="chien", command=correct)
B2 = tk.Button(dave, text="cheval", command=wrong)

# define position
L1.grid(row=0, column=0, columnspan=2)
B1.grid(row=1, column=0)
B2.grid(row=1, column=1)

dave.mainloop()
