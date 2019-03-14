from student_class import Student

class HighSchoolStudent(Student):
   school_name = "DAV high school"

   def get_school_name(self):             #Method overriding
      return "This is a high school student"

   def get_name_capitalize(self): #overriding method
      original_value = super().get_name_capitalize()   #we are calling get_name_capitalize from parent class.
      return original_value + "-HS"

