import HangAManPics as Pics
import tkinter as tk
import Run

carlos = tk.Tk()
# carlos.config(background="black") -- Dark mode be like

# Function to make the variable 'num' loop through values 0 to 6
def change():
    num.set((num.get()+1)%7) # update number and loops
    pic.set(Pics.get(num.get())) # show new image

fontInfo = ("verdana", 20)

# Picture number setup
num = tk.IntVar()
num.set(0)

# Text Label Number Setup
pic = tk.StringVar()
pic.set(Pics.get(num.get()))

# Label to show image
L1 = tk.Label(carlos, textvariable=pic, font=fontInfo)
L1.grid(row=0, column=0)

# Button to cycle through images
B1 = tk.Button(carlos, text="next", font=fontInfo, command=change)
B1.grid(row=1, column=0)

carlos.mainloop()
print(Run.end(True, False))