class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  

    def add_student(self, student):
        self.students.append(student)


# Testing the code
if __name__ == "__main__":
    cs3 = Course("Computer Science 3")

    s1 = Student("Apple", "2026-001")
    s2 = Student("Bob", "2026-002")

    cs3.add_student(s1)
    cs3.add_student(s2)

    print("Course:", cs3.course_name)
    for student in cs3.students:
        print("Student Name:", student.name, "| ID:", student.student_id)
