#!/usr/local/bin/python3
	
import sys
import subprocess
	
def mycom(command, *args):
   subprocess.call([command, args])
	
mycom(sys.argv[1], sys.argv[2], sys.argv[3])

