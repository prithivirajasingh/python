#!/usr/bin/env python3

import os
import sys
# import pyperclip

for item in sys.argv[1:]:
	if '-t=' in item:
		target = item[3:]
	if '-c' in item:
		filecount = int(item[2:])
		exitvar = 0
	else:
		# pyperclip.copy("Invalid argument")
		print('Invalid argument: {} \n'.format(item))

if not 'target' in locals():
	target = os.getcwd()
if not 'filecount' in locals():
	filecount = 5
	# exitvar = 1
if not 'exitvar' in locals():
	exitvar = 0

# pyperclip.copy(target)
# exit()
# print(target)
# exit()

if target == os.getenv("HOME"):
	print('This program is prohibited to be run in home folder. \nProgram will now exit. Modify program to override.')
	exit()

for folder, subfolders, files in os.walk(target):
	# print('Checkpoint 1')
	if folder != target:
		# print('Checkpoint 2')
		break
	for num in range(1, filecount + 1):
		filename = 'file' + str(num)
		filefound = 0
		for item in files:
			if item == filename:
				filefound = 1
				break
		if filefound == 0:
			cmd = 'touch ' + target + '/' + filename 
			print(cmd)
			# pyperclip.copy(cmd)
			os.system(cmd)
			if exitvar == 1:
				exit()
exit()

# Thunar menu ->
# /home/prithivi/bin/create_file.py -t=%f
