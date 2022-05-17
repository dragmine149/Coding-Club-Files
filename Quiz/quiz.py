import tkinter as tk

# canvas
root = tk.Tk()

# Sub routeens
def check():
    answer = ans.get()
    if answer == '3':
        result.set('Correct!')
    else:
        result.set('Incorect :(')

# font
mf = ('verdana', 30)

# string var input
ans = tk.StringVar()
result = tk.StringVar()
result.set('Waiting for answer...')

# Photo title
title = tk.PhotoImage(file = 'title.gif')
label = tk.Label(root, image = title)
label.grid(row = 0, column = 0, columnspan = 2)

# Question
questionLabel = tk.Label(root, text = '1 + 2?', font=mf)
questionLabel.grid(row = 1 , column = 0, columnspan = 2)

# Input argument
entry = tk.Entry(root, textvariable = ans, font=mf)
entry.grid(row = 2, column = 0)

# Output
output = tk.Label(root, textvariable = result, font=mf)
output.grid(row = 3, column = 0, columnspan = 2)

# Submit Button
button = tk.Button(root, text='Submit', font = mf, command = check)
button.grid(row = 2, column = 1)

# loop
root.mainloop()
