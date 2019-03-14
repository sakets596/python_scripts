#!/usr/local/bin/python3

#choice = 'y'
#all_users = []

def login(user):
   #print(user)
   try:
      f = open('database', 'r')
      for line in f.readlines():
         if(line == user):
            print(f"Welcome {user}")
            exit()
   except Exception:
      print("Unable to find this user in database")

   choice = input("you are not registered yet. Do you want to sign up(y/n): ")

   if(choice == 'y') or (choice == 'Y'):
      register(user)


def register(user):
   try:
      f = open('database', 'a')
      f.write(user)
      f.close()
      print(f"User {user} created successfully")
   except Exception:
      print("Couldn't create the user")


username = input("Hello!! please enter you username: ")
login(username)

