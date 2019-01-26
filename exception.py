#!/usr/local/bin/python3
student = {
   "name": "Mark",
   "student_id": 43215,
   "feedback": None
}

try:
   myvar=student["last_name"]
   #print(f"{myvar}")
except KeyError:
   print("Error finding lastname")


print("this code executes")
