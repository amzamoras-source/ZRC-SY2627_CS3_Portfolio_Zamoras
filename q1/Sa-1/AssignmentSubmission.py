class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date, is_submitted=False, grade=None):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = is_submitted 
        self.__grade = grade
        self.__submitted_files = []

    def __validate_grade(self, score):
        if score is not None and not 0 <= score <= 100:
            raise ValueError("Grade must be between 0 and 100")
        return score

    def __check_submission_status(self):
        if len(self.__submitted_files) > 0:
            self.__is_submitted = True

    def __is_duplicate(self, file_name):
        return file_name in self.__submitted_files

    def add_file(self, file_name):
        if self.__is_duplicate(file_name):
            print(f"[Warning]: File '{file_name}' already submitted!")
            return "File already submitted!"
    
        else:
            self.__submitted_files.append(file_name)
            self.__is_submitted = True
            print(f"[Success]: {self.student_name} added file '{file_name}'", "Total files submitted: " + str(len(self.__submitted_files)))
            
    def remove_file(self, file_name):
        if self.__grade is not None:
            print(f"[Error]: Cannot remove file '{file_name}' after grading!")

        elif file_name in self.__submitted_files and self.__grade is None:
            self.__submitted_files.remove(file_name)
            print(f"[Success]: {self.student_name} removed file '{file_name}'")

        else: 
            print(f"[Error]: File '{file_name}' not found in submission!")
            raise ValueError("File not found in submission")

    def assign_grade(self, score):
        if not self.__submitted_files:
            print(f"[Error]: Cannot assign grade to {self.student_name}. No files submitted!")
            return

        else:
            self.__grade = self.__validate_grade(score)
            print(f"[Success]: {self.student_name} has been assigned a grade of {self.__grade}")

    def get_grade(self):
        return self.__grade

    def view_files(self):
        if not self.__submitted_files:
            return '[Warning] No files submitted yet!'

        else:
            return f"Files submitted by {self.student_name}: {', '.join(self.__submitted_files)}"

    def get_status_report(self):
        submission_status = "Submitted" if self.__is_submitted else "Not Submitted"
        grade_status = self.__grade if self.__grade is not None else "Not Graded"
        return f"ID: {self.student_id:<13} | Name: {self.student_name:<15} | Status: {submission_status:<13} | Total Files: {len(self.__submitted_files):<2} | Grade: {grade_status}"


# --- INITIALIZING DROPBOX FOR STUDENTS ---
print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-103", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")

print("\n--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(student1.view_files())

print("\n--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.docx")
student2.assign_grade(88)
print(student2.view_files())

print("\n--- TEST SCENARIO 3: Preventing Duplicate File Submissions ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(student3.view_files())

print("\n--- TEST SCENARIO 4: Removing File after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print(student4.view_files())

print("\n--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) 
print(student5.view_files())

print("\n--- FINAL SYSTEM REPORTS ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
