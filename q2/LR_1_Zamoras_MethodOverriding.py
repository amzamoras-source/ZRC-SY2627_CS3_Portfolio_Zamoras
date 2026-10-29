# 1. Create the Python code that creates the parent class, Animal, and the child classes: Lion,
# Elephant, and Monkey, based on the given class diagram.
# 2. Override the eat() and make_sound() methods of the parent class Animal in the
# child classes: Lion, Elephant, and Monkey, to output the appropriate behavior of the animal.
# ● The lion roars loudly; the lion eats fresh meat.
# ● The elephant trumpets; the elephant eats grass and fruits.
# ● The monkey chatters; the monkey eats bananas.
# The object’s name must be included in the output texts, as shown below.
# 3. Create an object for each child's class and call the methods using a for loop.

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The", self.name, "makes a sound...")

    def eat(self):
        print("The", self.name, "eats...")

class Lion(Animal):
   super().make_sound()
   def make_sound(self):
    print("The", self.name, "roars loudly!")

   def eat(self):
    print("The", self.name, "eats fresh meat.")
    

class Elephant(Animal):


class Monkey(Animal):