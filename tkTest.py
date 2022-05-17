import tkinter as tk
dave = tk.Tk()  # canvas object
dave.title("Big Dave")
dave.geometry("500x500")

jon = tk.Label(dave, text = "Hello I am jon.")
pramil = tk.Label(dave, text = "Hello I am pramil.")

## It Code
jon.grid(row = 0, column = 0, sticky = 'w')
pramil.grid(row = 1, column = 0, sticky = 'w')

dave.mainloop()  # loops through for interaction
