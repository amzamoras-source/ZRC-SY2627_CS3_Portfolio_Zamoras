# Instruction: Do what is asked in each item below: 
# 1. Answer the following questions:
#      a.What is duck typing, as explained in the video?
# - Duck typing is a programming concept in which an object's suitability depends on the methods and attributes it has rather than its class or inheritance.

#      b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
# - The Car class needed to have a speak() method to work in the same loop as Dog and Cat, even without inheriting from Animal.

# 2. Create the Python code that:
# a. Creates three classes: Car, Boat, and Drone with a method move().
#              move() in the Car class  prints "The car drives on the road."
#             move() in the Boat class prints "The boat sails on water."
#              move() in the Drone class  prints "The drone flies in the sky."

# b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().

# c. Creates one object of each class. 

# d. Calls the start_trip() method for each object. 

# 3. How does the code in 2.2 demonstrate polymorphism?
# - The code demonstrates polymorphism because different objects can use the same method, move(), but produce different outputs depending on their respective classes.



class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)
