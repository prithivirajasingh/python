#!/usr/bin/env python3

userinput = input('Enter any key to continue, "a" to abort: ')
if userinput == 'a' or userinput == 'A':
	print("Program terminated by user.")
	exit()

print('Task started.')

import os
import sys

# print(sys.argv)
# print(len(sys.argv))
# print(os.getcwd())
# print('Separator')

for item in sys.argv[1:]:
	if item == 'True' or item == 'true':
		subfolder = True
	else:
		target = item

if not 'target' in locals():
	target = os.getcwd()
if not 'subfolder' in locals():
	subfolder = False

# print(subfolder)
# print(target)
# print(os.getenv("HOME"))
if target == os.getenv("HOME"):
	print('This program is prohibited to be run in home folder. \nProgram will now exit. Modify program to override.')
	exit()

charlist = [' ', '\\', '[', ']', '(', ')', '\'', '!', '+', '-']
trans1 = ''.join(charlist)
trans2 = '_' * len(charlist)
transdict = ''.maketrans(trans1, trans2)
# print(trans1)
# print(trans2)
# print(transdict)
# exit()

count = 0
while count > 0:
	for folder, subfolders, files in os.walk(target):
		# print('\nFolder is :' + folder)
		if folder != target and subfolder == False:
			break

		for item in files:
			premod = os.path.join(folder, item)
			# print(premod + '\n')
			if any(chars in item for chars in charlist):
				# print(premod)
				tempstring = item.translate(transdict)
				templist = tempstring.split('_')
				# print(templist)
				templist = list(filter(None, templist))
				# print(templist)
				tempstring = '_'.join(templist)
				tempstring = tempstring.replace('_.','.')
				tempstring = tempstring.replace('...','.')
				tempstring = tempstring.replace('..','.')
				tempstring = tempstring.replace('___','_')
				tempstring = tempstring.replace('_+_','_')
				tempstring = tempstring.replace('_-_','_')
				postmod = os.path.join(folder, tempstring)
				# print(postmod)
				cmd = 'mv "' + premod + '" ' + postmod
				print(premod)
				# print(cmd + '\n')
				# os.system(cmd)
				count += 1

		for item in subfolders:
			premod = os.path.join(folder, item)
			# print(premod + '\n')
			if any(chars in item for chars in charlist):
				# print(premod)
				tempstring = item.translate(transdict)
				templist = tempstring.split('_')
				# print(templist)
				templist = list(filter(None, templist))
				# print(templist)
				tempstring = '_'.join(templist)
				tempstring = tempstring.replace('_.','.')
				tempstring = tempstring.replace('...','.')
				tempstring = tempstring.replace('..','.')
				tempstring = tempstring.replace('___','_')
				tempstring = tempstring.replace('_+_','_')
				tempstring = tempstring.replace('_-_','_')
				postmod = os.path.join(folder, tempstring)
				# print(postmod)
				cmd = 'mv "' + premod + '" ' + postmod
				print(premod)
				# print(cmd + '\n')
				# os.system(cmd)
				count += 1
print('Task completed.')