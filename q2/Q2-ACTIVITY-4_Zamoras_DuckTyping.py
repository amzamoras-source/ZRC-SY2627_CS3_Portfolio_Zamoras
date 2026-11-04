# Instructions:  Create the Python code that:

# Has three classes: HealthPotion, ManaPotion, SpeedBoost.
#      Each class should have a method called use():
#      HealthPotion’s use() method  prints "You regain 50 HP!"
#      ManaPotion’s use() method prints "You restore 30 MP!"
#      SpeedBoost’s use() method  prints "Your speed increases for 10 seconds!"
# Has a function apply_item(item), with the parameter item,  that calls the method use() :  item.user();

# Creates one object of each class.

# Stores the objects in a list, potions,  and calls apply_item() for each object using a loop.

# Sample Output: 

# You regain 50 HP!
# You restore 30 MP!
# Your speed increases for 10 seconds!


class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

health = HealthPotion()
mana = ManaPotion()
speed = SpeedBoost()

potions = [health, mana, speed]

for item in potions:
    apply_item(item)
