# Instructions: Create the Python code that:

# 1. Has three classes: Warrior, Mage, Archer.

#             Each class has a method called special_move().

#             Warrior special_move()  method in prints “Warrior swings a mighty sword!”

#             Mage special_move()  method prints “Mage casts a powerful spell!”

#             Archer special_move()  method prints "Archer shoots a precise arrow!"

# 2. Has a function perform_move(character), with the parameter character,  that calls the method special_move() :  character.special_move().

# 3. Creates one object of each class.

# 4. Stores the objects in a list, named characters,  and calls perform_move() for each object using a loop.

# Sample Output: 

# Warrior swings a mighty sword!
# Mage casts a powerful spell!
# Archer shoots a precise arrow!


class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

warrior = Warrior()
mage = Mage()
archer = Archer()

characters = [warrior, mage, archer]

for character in characters:
    perform_move(character)
