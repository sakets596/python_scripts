#!/usr/local/bin/python3

flag = 0

def login(user):
   #print(user)
   try:
      f = open('database', 'r')
      for line in f.readlines():
         if(line == (user + "\n")): #/n is required because at the end of all users there is /n character.
            print(f"Welcome {user}")
            flag = 1
      if (flag == 1):
         opt = input("What you want to do?\n1. Addition")
         if(opt == 1):
            add()
      
   #except Exception:
     # print("Unable to find this user in database")
      else:
         choice = input("you are not registered yet. Do you want to sign up(y/n): ")

   if(choice == 'y') or (choice == 'Y'):
      register(user)
   elif(choice == 'n') or (choice == 'N'):
      exit()
   else:
      print("invalid choice")


def register(user):
   try:
      f = open('database', 'a')
      f.write(user + "\n")
      f.close()
      print(f"User {user} created successfully")
   except Exception:
      print("Couldn't create the user")

def add(number1, number2):
   sum = number1 + number2
   return sum


username = input("Hello!! please enter you username: ")
login(username)


