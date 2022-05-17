import random

# Make a new class for the character
class character:

    # Set the character up to start with.
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    # Returns the character name
    def getName(self):
        return self.name

    # Retruns the character strength
    def getStrenght(self):
        return self.strenght
    
    # Returns the character health
    def getHealth(self):
        return self.health

    # Changes the character health by X
    def changeHealth(self, ammount):
        self.health += ammount


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
