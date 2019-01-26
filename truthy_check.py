#!/usr/local/bin/python3
number=5
if number:
   print(f"No {number} is a truthy value")
else:
   print(f"No {number} is not a truthy value")

number=-20
if not number:
   print(f"No {number} is not a truthy value")
else:
   print(f"No {number} is a truthy value")

number=0
if number:
   print(f"No {number} is a truthy value")
else:
   print(f"No {number} is not a truthy value")

str="Saket"
if str:
   print(f"String {str} is a truthy value")
else:
   print(f"String {str} is not a truthy value")

str=""
if str:
   print(f"String {str} is a truthy value")
else:
   print(f"String {str} is not a truthy value")
