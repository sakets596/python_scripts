#!/usr/local/bin/python3

import time
import os

def destruct():
   for i in range(10, 0, -1):
      print(f"{i}")
      time.sleep(1)
      os.system('clear')
   print("Kaboom")

destruct()   
