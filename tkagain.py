import tkinter as tk

# Canvas
dave = tk.Tk()

# Greet subrouteen
def greet():
    personsname = v.get()
    if personsname is not "":
        v2.set("Hello " + personsname)

# Variables
v = tk.StringVar()
v2 = tk.StringVar()
v2.set("Hi!")

# Label for name
labelName = tk.Label(dave, text="Enter Name: ")
labelName.grid(row=0, column=0)

# Label for name
labelName = tk.Entry(dave, textvariable=v)
labelName.grid(row=0, column=1)

# Button to submit
button = tk.Button(dave, text="Submit", command=greet)
button.grid(row=1, column=0)

# Output
outLabel = tk.Label(dave, textvariable=v2)
outLabel.grid(row=1, column=1)

dave.mainloop()
