#!/usr/local/bin/python3

#reading file
def read(file):
   try:
      f = open(file, "r")
      for line in f.readlines():
         print(line)
      f.close()
   except Exception:
      print("unable to read the file")


def write(file, name):
   try:
      f = open(file, "a")
      f.write(name + "\n")
      f.close()
      print("Successfully wrote on the file")
   except Exception:
      print("Couldn't write on the file")

c = input("What do you want to do?\n\n1. Read file\n2. Write\n\n") # variable c  will store value as string
choice = int(c)   #var c is in string, converting it to int.

if(choice == 1):
   file = input("Enter the file name: ")
   read(file)
   #print("you have enterd 1")

elif(choice == 2):
   file = input("Enter the file name to write on: ")
   name = input("Enter the name of the student: ")
   write(file, name)

else:
   print("Wrong choice")

