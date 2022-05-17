import tkinter as tk

# Canvas setup
dave = tk.Tk()

# next Slide -> adds 1 to the image to go to the next image.
def nextSlide():
    number.set((number.get() + 1) % len(hangmanImages)) # reset to 0
    print(f'DEBUG -> {number.get()}') # debug, just checking if the number is actually go up. Not needed
    L1.configure(image=hangmanImages[number.get()]) # Display the new image


# setting up the list -> From 'Hang1' to 'Hang10'
hangmanImages = []
for i in range(1, 11):
    hangmanImages.append(tk.PhotoImage(file = f"hang{i}.gif")) #py 3.6+ warning

# number setup (slide view)
number = tk.IntVar()
number.set(0)

# UI
L1 = tk.Label(dave, image = hangmanImages[number.get()])
L1.grid(row = 0, column = 0)
B1 = tk.Button(dave, image=tk.PhotoImage(file = "Next.gif"), command=nextSlide)
B1.grid(row = 1, column = 0)

dave.mainloop()