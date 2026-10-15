# Instruction:
# For each situation below, decide whether the attribute should be public, protected, or private,
# then write the correct Python statement to declare the attribute inside the __init__()
# constructor method. Do these on your notebook.

# 1. A GameCharacter class has a username that can be displayed and accessed by anyone.
#This attribute should be public.

class GameCharacter:
    def __init__(self, username):
        self.username = username  # public attribute

# 2. A BankAccount class has a balance that should NOT be accessed directly outside the class.
# This attribute should be private.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

# 3. A Vehicle class has an engineCode that should only be accessed within the class and its subclasses.
# This attribute should be protected.

class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode  # protected attribute


# 4. A Student class has a schoolName that is safe for everyone to view and modify.
# This attribute should be public.

class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName  # public attribute

# 5. A VotingSystem class has a voterID that must be hidden for security reasons.
# This attribute should be private.

class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID  # private attribute