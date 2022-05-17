import random as r
import tkinter as tk
mf = ("helvetica", 0)

def roll():
    num.set(r.randint(1,6))

# canvas
window = tk.Tk()

# Value
num = tk.IntVar()
roll()

# Label
dice = tk.Label(window, textvariable=num, font=mf)
dice.grid(row=0, column=0)

# Button
Buzzer = tk.Button(window, text="Press Me", font=mf, command=roll)
Buzzer.grid(row=1, column=0)

# loop
window.mainloop()
