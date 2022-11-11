"""
MAKING BUTTONS IN TKINTER
"""

import tkinter as tk

Graham = tk.Tk()

Message = tk.StringVar()

f1 = ("verdana", 20)


def test():
    Message.set("hi")


L1 = tk.Label(Graham, textvariable=Message, font=f1)
B1 = tk.Button(Graham, text="Press Me!", font=f1, command=test)
L1.grid(row=0, column=0)
B1.grid(row=1, column=0)

Graham.mainloop()
