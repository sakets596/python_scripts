#!/usr/local/bin/python3

students = []

class Student:
   def __init__(self, name, student_id = 332):
      self.name = name
      self.student_id = student_id
      students.append(self)

   def __str__(self):
      return "Student " + self.name

   def get_name_capitalize(self):
      return self.name.capitalize()

   def get_student_id(self):
      return self.student_id

mark = Student("mark", 657)
#print(mark)
#print(f"Student name is:", mark.get_name_capitalize())
#print (f"Student id is :", mark.get_student_id())

print(dir(students))

