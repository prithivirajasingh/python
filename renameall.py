#!/usr/bin/env python3

import os
import sys
import pymsgbox
import time

# print(sys.argv)
# print(len(sys.argv))
# print(os.getcwd())
# print('Separator')

for item in sys.argv[1:]:
	if item == 'True' or item == 'true':
		subfolder = True
	else:
		target = sys.argv[1]

if not 'target' in locals():
	target = os.getcwd()
if not 'subfolder' in locals():
	subfolder = False
else:
	subfolder = True

# print(subfolder)
# print(target)

charlist = [' ', '\\', '[', ']', '(', ')']
trans1 = ''.join(charlist)
trans2 = '_' * len(charlist)
transdict = ''.maketrans(trans1, trans2)
# print(trans1)
# print(trans2)
# print(transdict)
# exit()


for folder, subfolders, files in os.walk(target):
	# print('\nFolder is :' + folder)
	if folder != target and subfolder == False:
		break

	for item in files:
		premod = os.path.join(folder, item)
		if any(chars in premod for chars in charlist):
			# print(premod)
			postmod = premod.translate(transdict)
			templist = postmod.split('_')
			# print(templist)
			templist = list(filter(None, templist))
			# print(templist)
			postmod = '_'.join(templist)
			postmod = postmod.replace('_.','.')
			# print(postmod)
			cmd = 'mv "' + premod + '" ' + postmod
			# print(cmd)
			os.system(cmd)

	for item in subfolders:
		premod = os.path.join(folder, item)
		if any(chars in premod for chars in charlist):
			# print(premod)
			postmod = premod.translate(transdict)
			templist = postmod.split('_')
			# print(templist)
			templist = list(filter(None, templist))
			# print(templist)
			postmod = '_'.join(templist)
			postmod = postmod.replace('_.','.')
			# print(postmod)
			cmd = 'mv "' + premod + '" ' + postmod
			# print(cmd)
			os.system(cmd)
