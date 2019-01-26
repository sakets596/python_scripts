#!/usr/local/bin/python3
students = []

def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase.append(student["name"].title()) #//we are not using student.title because student
                                                     # is a dir and not a string
     
    return student_titlecase


def print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)

def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def save_file(student):
    try:
       f = open("students.txt", "a")
       f.write(student + "\n")
       f.close()
    except Exception:
       print("could not save file")
		 
		 
def read_file():
    try:
       f = open("students.txt", "r")
       for student in f.readlines():
          add_student(student)
       f.close()
    except Exception:
       print("Could not read file")
		


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)

save_file(student_name)
