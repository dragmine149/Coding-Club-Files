from tkinter import *
import Run

def click(num):
    print(num)
    display.set(f"Button Clicked: {num}")

dave = Tk()
display = StringVar()
L1 = Label(dave, textvariable=display)
L1.grid(row=0, column=0, columnspan=5)

Buttons = []
commands = []
def genButton():
    for i in range(10):
        tempB = Button(dave, text=str(i), command= lambda i=i: click(i)) # Curtisy of https://stackoverflow.com/a/10865170.
        if i > 4:
            tempB.grid(row=2, column=i-5)
        else:
            tempB.grid(row=1, column=i)
        Buttons.append(tempB)

genButton()

dave.mainloop()
print(Run.end(True, False))