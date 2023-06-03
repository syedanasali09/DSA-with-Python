class Student:
    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age):
        student = Student(roll_no, name, age)
        self.students.append(student)
        print("Student added successfully!")

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student removed successfully!")
                return
        print("Student not found!")

    def display_students(self):
        if not self.students:
            print("No students found!")
            return

        print("Student List:")
        for student in self.students:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}")

# Example usage:
sms = StudentManagementSystem()

# Add students
sms.add_student(101, "Humais", 18)
sms.add_student(102, "Ali", 20)
sms.add_student(103, "Sayyaf", 19)

# Display students
sms.display_students()

# Remove a student
sms.remove_student(102)

# Display students again
sms.display_students()
