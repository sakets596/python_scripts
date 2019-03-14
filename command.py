#!/usr/local/bin/python3

import sys
import subprocess

def mycom(command, option):
   subprocess.call([command, option])

mycom(sys.argv[1], sys.argv[2])
