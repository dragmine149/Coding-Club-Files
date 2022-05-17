import tkinter as tk
import random
import time
import sys
import Run

# Create frame / ui
cat = tk.Tk("Typing Test")
cat.title("Typing Test")

# List of words to cycle through.
# Word list from: https://www.ef.co.uk/english-resources/english-vocabulary/top-1000-words/
words = []
with open("words.txt", "r") as wordList:
    words = wordList.readlines()

# Create variables for later use
word = tk.StringVar()
newWord = random.randint(0, len(words))
word.set(words[newWord].rstrip())

result = tk.StringVar()
result.set("Waiting...")
inputVar = tk.StringVar()

# Font to make things readable
font = ("verdana", 20)

# Function to check if inputed value is equal to the required value and reset if true.
# else gets them to reenter the value.
def Submit():
    if inputVar.get().rstrip() == word.get().rstrip():
        result.set("Correct! Well done!")
        inputVar.set("")
        # If correct and more words
        if len(words) > 0:
            # Replace word with new word
            words.pop(words.index(word.get() + '\n'))
            newWord = random.randint(0, len(words))
            word.set(words[newWord].rstrip())
        else:
            # pritn well done and exit
            time.sleep(1)
            result.set("Well done, All words have been cleared")
            sys.exit(f"Compelted list in {Run.end(False)} seconds")
    else:
        # reset if incorrect
        result.set("Incorrect, Please try again")
        inputVar.set("")

# Display layout and make
wordLabel = tk.Label(cat, textvariable=word, font=font)
wordLabel.grid(row=0, column=0)

outLabel = tk.Label(cat, textvariable=result, font=font)
outLabel.grid(row=1, column=0)

entry = tk.Entry(cat, textvariable=inputVar, font=font)
entry.grid(row=2, column=0)

button = tk.Button(cat, text="Submit", command=Submit, font=font)
button.grid(row=3, column=0)

cat.mainloop()

print(f"Stopped after: {Run.end(False)} seconds")