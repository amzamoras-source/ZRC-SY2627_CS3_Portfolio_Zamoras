

#UPDATED VERSION WITH PATIENT TYPE DISPLAYED

# Coding Assessment: Hospital Billing System
# Goal: Apply encapsulation, inheritance, and method overriding in Python to create a hospital
# billing system that calculates different discounts based on patient type.
# Role: You are a Junior Software Developer hired by a hospital to improve their billing system.
# Audience: The Hospital Administration Team needs an automated way to accurately and fairly
# compute patient bills.
# Situation: The hospital serves different types of patients:
# Regular Patients pay the full amount.
# Senior Citizens receive a 20% discount.
# PhilHealth Members receive 15% discount.
# Currently, billing is done manually, which causes delays and errors.
# Product: A system using encapsulation, inheritance, and method overriding to automate
# billing computation.
# Your task is to create a Python program that:
# 1. Creates a parent class Patient with the following features
# Attributes: name, bill_amount
# Methods: Getter and setter methods and
# calculate_bill() (returns full bill)

# 2. Creates child classes:
# SeniorPatient
# PhilHealthPatient
# 3. Overrides the calculate_bill() method in each subclass to apply the correct discount.
# (Refer to the class diagram for the features of each class.)

# **Sample output:**

# Hospital Billing System
# -----------------------
# Patient Name:  Juan Dela Cruz
# Original Bill: ₱15,000.00
# Final Bill: ₱15,000.00

# Patient Name:  Maria Santos
# Original Bill: ₱15,000.00
# Final Bill: ₱12,000.00

# Patient Name:  Pedro Reyes
# Original Bill: ₱15,000.00
# Final Bill: ₱12,750.00

# class Patient:
#     def __init__(self, name, bill_amount):
#         self.__name = name
#         self.__bill_amount = bill_amount

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_bill_amount(self):
#         return self.__bill_amount

#     def set_bill_amount(self, bill_amount):
#         self.__bill_amount = bill_amount

#     def calculate_bill(self):
#         return self.__bill_amount

#     def display_patient_type(self):
#         return "Regular Patient"


# class Senior_Patient(Patient):
#     def calculate_bill(self):
#         return self.get_bill_amount() * 0.80

#     def display_patient_type(self):
#         return "Senior Patient"


# class PhilHealth_Patient(Patient):
#     def calculate_bill(self):
#         return self.get_bill_amount() * 0.85

#     def display_patient_type(self):
#         return "PhilHealth Patient"


# p1 = Patient("Juan Dela Cruz", 15000.00)
# p2 = Senior_Patient("Maria Santos", 15000.00)
# p3 = PhilHealth_Patient("Pedro Reyes", 15000.00)

# print("Hospital Billing System")
# print("-----------------------")

# print("Patient Name:  " + p1.get_name())
# print(f"Patient Type:  {p1.display_patient_type()}")
# print(f"Original Bill: ₱{p1.get_bill_amount():,.2f}")
# print(f"Final Bill: ₱{p1.calculate_bill():,.2f}\n")

# print("Patient Name:  " + p2.get_name())
# print(f"Original Bill: ₱{p2.get_bill_amount():,.2f}")
# print(f"Patient Type:  {p2.display_patient_type()}")
# print(f"Final Bill: ₱{p2.calculate_bill():,.2f}\n")

# print("Patient Name:  " + p3.get_name())
# print(f"Original Bill: ₱{p3.get_bill_amount():,.2f}")
# print(f"Patient Type:  {p3.display_patient_type()}")
# print(f"Final Bill: ₱{p3.calculate_bill():,.2f}")


# Situation: Your Science Lab Inventory System needs a way to handle different sensors (Temperature, pH, and Light).

# Tasks: 

# Use the code from the last session to create an Abstract Base Class called Sensor.
# Give it an abstract method called get_reading().
# Create two child classes: PHSensor and TempSensor.
# Implement the get_reading() method in both so they print their specific type of data.
# Try to create an object of the Sensor class directly. What does Python tell you?

# Expected Terminal Output

# When your code is finished and running correctly, your terminal should look something like this:

# For Tasks 1–4 (The Success Run):

# --- Lab Inventory System ---
# [pH Sensor] Reading: 7.2 pH (Neutral)
# [Temperature Sensor] Reading: 24.5°C

# ----------------------------

# For Task 5 (The "Break it" Test):

# If you try to write my_sensor = Sensor(), Python should "scream" at you with a specific error. Students should look for this:

# TypeError: Can't instantiate abstract class Sensor with abstract method get_reading

from abc import ABC, abstractmethod


class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


class PHSensor(Sensor):
    def __init__(self, result, reading):
        self.result = result
        self.reading = reading

    def get_reading(self):
        return f"{self.result} ({self.reading})"


class TempSensor(Sensor):
    def __init__(self, temperature):
        self.temperature = temperature

    def get_reading(self):
        return self.temperature


# my_sensor = Sensor()


class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        return "Regular Patient"


class Senior_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        return "Senior Patient"


class PhilHealth_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        return "PhilHealth Patient"


p1 = Patient("Juan Dela Cruz", 15000.00)
p2 = Senior_Patient("Maria Santos", 15000.00)
p3 = PhilHealth_Patient("Pedro Reyes", 15000.00)
temperature = TempSensor("24.5°C")
result = PHSensor("7.2 pH", "Neutral")
# sensor = Sensor("Sense")

print("Hospital Billing System")
print("-----------------------")

print("Patient Name:  " + p1.get_name())
print(f"Patient Type:  {p1.display_patient_type()}")
print(f"Original Bill: ₱{p1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p1.calculate_bill():,.2f}\n")

print("Patient Name:  " + p2.get_name())
print(f"Original Bill: ₱{p2.get_bill_amount():,.2f}")
print(f"Patient Type:  {p2.display_patient_type()}")
print(f"Final Bill: ₱{p2.calculate_bill():,.2f}\n")

print("Patient Name:  " + p3.get_name())
print(f"Original Bill: ₱{p3.get_bill_amount():,.2f}")
print(f"Patient Type:  {p3.display_patient_type()}")
print(f"Final Bill: ₱{p3.calculate_bill():,.2f}")
print("                                          ")
print("                                          ")


print("--- Lab Inventory System ---")
print("                                           ")
# print("Sensor: {sensor.get_reading()}")
print(f"[pH Sensor] Reading: {result.get_reading()}")
print(f"[Temp Sensor] Reading: {temperature.get_reading()}")
print("                                           ")
print("----------------------------")
# my_sensor = Sensor()





        



        
    

        
    