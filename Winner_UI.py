import Run
import Winner
import tkinter as tk

canvas = tk.Tk()

Labels = [
    tk.Label(canvas, text=num1),
    tk.Label(canvas, text=num2),
    tk.Label(canvas, text=num3),
    tk.Label(canvas, text=num4),
    tk.Label(canvas, text=num5),
    tk.Label(canvas, text=num6)]

def AddToUi(List):
    for value in range(len(x)):
        label = tk.Label(canvas, text=num[value])
        label.grid(row=0, column=value + 2)

def genereate():
    AddToUi(Winner.Select())

button = tk.Button(canvas, text="Pick Numbers", command=genereate)
button.grid(row=0, column=0)

x = Winner.Select()
AddToUi(x)
print(x)

canvas.mainloop()

print(Run.end(True, False))
