class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []
    
    def __validate_grade(self, score: float):
        if score < 0 or score > 100:
            return False
        return True

    def __check_submission_status(self):
        return len(self.__submitted_files) > 0

    def __is_duplicate(self, file_name: str):
        return file_name in self.__submitted_files

    def add_file(self, file_name: str):
        if self.__grade is not None:
            raise ValueError(f"{self.student_name} cannot add files. Assignment already graded.")
        if not isinstance(file_name, str) or not file_name.strip():
            raise ValueError("File name must be a non-empty string.")
        if self.__is_duplicate(file_name):
            raise ValueError(f"'{file_name}' is already attached!")
        self.__submitted_files.append(file_name)
        self.__is_submitted = self.__check_submission_status()
        print(f"[Success] {self.student_name} attached '{file_name}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, file_name: str):
        if self.__grade is not None:
            raise ValueError(f"{self.student_name} cannot remove files. Assignment already graded.")
        if file_name in self.__submitted_files:
            self.__submitted_files.remove(file_name)
            self.__is_submitted = self.__check_submission_status()
            print(f"[Success] {self.student_name} removed '{file_name}'.")
        else:
            raise ValueError(f"File '{file_name}' not found in submitted files.")

    def assign_grade(self, score: float):
        if not self.__validate_grade(score):
            raise ValueError("Grade must be between 0 and 100.")
        if not self.__check_submission_status():
            raise ValueError(f"Cannot grade. No files submitted for {self.student_name}.")
        self.__grade = score
        print(f"[Success] Grade {score} officially assigned to {self.student_name}.")

    def get_grade(self) -> str:
        return "Not Graded" if self.__grade is None else f"{self.__grade}"

    def view_files(self) -> str:
        return ", ".join(self.__submitted_files) if self.__submitted_files else "No files submitted"

    def get_status_report(self):
        status = "Submitted" if self.__is_submitted else "Missing"
        return (f"ID: {self.student_id} | Name: {self.student_name} | "
            f"Status: {status} ({len(self.__submitted_files)} files) | "
            f"Grade: {self.get_grade()}")

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(
    student_name="Alex Gonzaga", 
    student_id="pshs-1090-x", 
    assignment_title="CS-101", 
    due_date="2026-10-01"
)
student2 = AssignmentSubmission(
    student_name="Adelle", 
    student_id="pshs-1920-x", 
    assignment_title="CS-103", 
    due_date="2026-10-01"
)
student3 = AssignmentSubmission(
    student_name="Juan dela Cruz", 
    student_id="pshs-1033-x", 
    assignment_title="CS-101", 
    due_date="2026-10-01"
)
student4 = AssignmentSubmission(
    student_name="Maria Santos", 
    student_id="pshs-1044-x", 
    assignment_title="CS-101", 
    due_date="2026-10-01"
)
student5 = AssignmentSubmission(
    student_name="Jose Reyes", 
    student_id="pshs-1055-x", 
    assignment_title="CS-101", 
    due_date="2026-10-01"
)
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
try:
    student3.add_file("script.py")
except ValueError as error:
    print(f"[Warning] {error}")
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
try:
    student4.remove_file("exam_answers.pdf")
except ValueError as error:
    print(f"[Warning] {error}")
print()

print("--- TEST SCENARIO 5: Empty List  Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
try:
    student5.assign_grade(100)
except ValueError as error:
    print(f"[Error] {error}")
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())