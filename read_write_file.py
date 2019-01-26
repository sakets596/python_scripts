#!/usr/local/bin/python3
def file_write(name="Unknown"):
   try:
      f=open("mylist1", "a")
      f.write(name + "\n")
      f.close()
      print("Successfully written in the file mylist1")
   except Exception:
      print("Could not write on the file mylist1")


def file_read():
   try:
      f=open("mylist1", "r")
      for line in f.readlines():
         print(line)
      f.close
   except:
      print("Could not read from the file mylist1")

#file_write()
#file_read()



while True:
   opt=input("Do you want to continue(y/n)?: ")
   if(opt == "y" or opt == "Y"):
      name=input("Enter the name of the student: ")
      file_write(name)
      #print("Below are the list of the students:")
   else:
      print("Below are the list of the students")
      file_read()
      exit()
