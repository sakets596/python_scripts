#!/usr/local/bin/python3
def read_file():
   try:
      f=open("myfile1", "r")
      for i in f.readlines():
         print(i)
   except Exception:
      print("could not open the file")

read_file()
