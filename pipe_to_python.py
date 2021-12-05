#!/usr/bin/python
import sys
import subprocess

def hello(variable):
   print variable

data = sys.stdin.read()
hello(data)
