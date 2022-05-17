import Run

def replace_vowels(word, char):
    newWord = ""
    vowels = "aeiou"
    for i in range(len(word)):
        newLetter = word[i]
        if newLetter in vowels:
            newLetter = char
        newWord += newLetter

    return newWord
    
if __name__ == "__main__":
    print(replace_vowels("hello", "?"))
    print(replace_vowels("The quick brown fox jumps over the lazy dog", "?"))

    print(Run.end(True, False))
