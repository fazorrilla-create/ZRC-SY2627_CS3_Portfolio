# Write a short Python code snippet showing a Course adding a Student object to a list. 

class Student:
    def __init__(self, name, grade_level, student_number):
        self.name = name
        self.grade_level = grade_level
        self.student_number = student_number

    def displayInfo(self):
        return f"{self.name} - Grade {self.grade_level} - ID: {self.student_number}"


class Course:
    def __init__(self, course_name, teacher, room):
        self.course_name = course_name
        self.teacher = teacher
        self.room = room
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def displayCourse(self):
        print(f"\nCourse: {self.course_name}")
        print(f"Teacher: {self.teacher}")
        print(f"Room: {self.room}")
        print("Students:")

        for student in self.students:
            print("-", student.displayInfo())


student1 = Student("Franz", 9, "SOD-001")
student2 = Student("Reiahe", 9, "SOD-002")
student3 = Student("Dasha", 8, "SOD-003")

course = Course("Computer Science", "Sir Bon", "CS Lab")

course.addStudent(student1)
course.addStudent(student2)
course.addStudent(student3)

course.displayCourse()