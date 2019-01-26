#!/usr/local/bin/python3
students = []

class Student:
   def __init__(self, name, student_id=332):
      student = {"name": name, "student_id": student_id}
      students.append(student)

mark = Student("Mark")
print(students)
print(mark)
