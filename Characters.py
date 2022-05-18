import random
import os

# Make a new class for the character
class character:

    # Set the character up to start with.
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        self.alive = True

    # Returns the character name
    def getName(self):
        return self.name

    # Retruns the character strength
    def getStrength(self):
        return self.strength
    
    # Returns the character health
    def getHealth(self):
        return self.health

    # Changes the character health by X
    def changeHealth(self, ammount):
        self.health += ammount
        if self.health <= 0:
            self.alive = False


sayu = character('sayu', 10, 100)
qiqi = character('qiqi', 8, 150)

# Tests
print(sayu.getHealth())
print(sayu.changeHealth(-2))
print(sayu.getHealth())
print(sayu.changeHealth(4))
print(sayu.getHealth())

print('--------------------------------')

# Random health thing
print(f'{sayu.getName()}! You got hit!')
health = random.randint(1,6)
sayu.changeHealth(-health)
print(f'{sayu.getName()} Your health is now {sayu.getHealth()}')

def tree():
    answer = None
    while answer is None:
        answer = input("You see a tree! Do you attack or hug?: ")
        if answer.lower() == "hug":
            print("The tree healed you!")
            sayu.Health = 100
        elif answer.lower() == "attack":
            print("The tree attacked back!")
            sayu.changeHealth(-1)
        else:
            print("Please enter a valid input")

def qiqiE():
    while qiqi.alive:
        print("You spot a wild qiqi")
        print("You automaticall attack qiqi")
        sayu.changeHealth(-qiqi.getStrength())
        qiqi.changeHealth(-sayu.getStrength())

encourtments = [tree, qiqiE]

os.system('clear')  # get rid of old stuff, not needed.
while sayu.alive:
    item = random.randint(0, len(encourtments))
    encourtments[item -1]()
