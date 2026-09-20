# This code will showcase a practice of using the class keyword in Python.

print("Hey there! Welcome to the class.")

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


def pick_Student():
    print("Let's pick a student to display their information.")
    print("1. Alice")
    print("2. Bob")
    print("3. Charlie")
    choice = input("Enter the number of the student you want to pick (1-3): ")

    if choice == '1':
        student1.display_info()
        student1.introduce()
    elif choice == '2':
        student2.display_info()
        student2.introduce()        
    elif choice == '3':

        student3.display_info()
        student3.introduce()
                

student1 = student("Alice", 20)
student2 = student("Bob", 22)
student3 = student("Charlie", 19)


pick_Student()
