#!/usr/local/bin/python3

students = []

class Student:
   def add_student(self, name, student_id=332):      #self refers to the instance of the class.
      student = {"name": name, "student_id": student_id}
      students.append(student)


# self.add_student("Mark") #This is why we use self, and this is how we use recursion

student = Student()
student.add_student("Mark")

print(students)
