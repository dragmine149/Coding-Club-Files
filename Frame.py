import tkinter as tk

john = tk.Tk("Frame Test")
john.title("Frame Test")  # titling the frame to let the user know what the frame does (without looking at the code)

# FRAMES, the purpose of this
frame1 = tk.Frame(john)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(john)
frame2.grid(row=0, column=1)

# Font libarary
fonts = [
    ("verdaba", 20)
]

# Just some basic labels
# This time, instead of parent under root 'john' we put them under frames
label1 = tk.Label(frame1, text="yes!", font=fonts[0])
label1.grid(row=0, column=0)

label2 = tk.Label(frame1, text="Lucas", font=fonts[0])
label2.grid(row=0, column=1)

label3 = tk.Label(frame1, text="no!", font=fonts[0])
label3.grid(row=1, column=0)

label4 = tk.Label(frame1, text="Dan", font=fonts[0])
label4.grid(row=1, column=1)

# 8k Dog...
file = tk.PhotoImage(file="dog2.gif")  # doesn't like being in the tk.label...
image = tk.Label(frame2, image=file)
image.grid(row=0, column=0)  # new frame so differnet grid position

john.mainloop()