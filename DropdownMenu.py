import tkinter as tk

# Submit button function
def submitFunc():
    print(dog.get())

# make ui
root = tk.Tk("Dropdown Menu")
root.title("Dropdown Menu")

# Data for the dropdown menu
data=["chow chow",
     "besengie",
     "St Bernard"]

# Make variable
dog = tk.StringVar()
dog.set(data[0])  # set to first item in the list for easy changing.
font = ("verdana", 20)

# Make the dropdown menu.
# NOTE: the normal font `font=font` doesn't work in this menu
steve = tk.OptionMenu(root, dog, *data)
steve.grid(row=0, column=0)

# Make submit button
button = tk.Button(root, text="Submit", font=font, command=submitFunc)
button.grid(row=0, column=1)

root.mainloop()