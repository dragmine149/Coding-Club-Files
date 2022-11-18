import tkinter as tk

# NOTE: IMAGES ARE NOT MINE IN ANY WAY SHAPE OR FORM

mark = tk.Tk()

# make photoimage objects to show images on the ui
cat = tk.PhotoImage(file="gifs/cat.gif")
animal= tk.PhotoImage(file="gifs/animal.gif")
giraffe = tk.PhotoImage(file="gifs/giraffe.gif")
dog = tk.PhotoImage(file="dog2.gif")

# show the images on the ui
l1 = tk.Label(mark, image=cat)
l1.grid(row=0, column=0)
l2 = tk.Label(mark, image=animal)
l2.grid(row=0, column=1)
l3 = tk.Label(mark, image=giraffe)
l3.grid(row=1, column=0)
l4 = tk.Label(mark, image=dog)
l4.grid(row=1, column=1)

mark.mainloop()
