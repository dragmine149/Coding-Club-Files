import tkinter as tk

# Canvas
Dave=tk.Tk()

f1 = ("helvetica", 20)

Dave.geometry("500x300")
L1 = tk.Label(Dave, text="Hello World", font=f1)
L1.grid(row=0, column=0)
L2 = tk.Label(Dave, text="Goodbye", font=f1)
L2.grid(row=0, column=0)

Dave.mainloop()