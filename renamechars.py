#!/usr/bin/env python3

# userinput = input('Enter any key to continue, "a" to abort: ')
if not 'userinput' in locals():
	userinput = 'y'
# print(userinput)
if userinput == 'a' or userinput == 'A':
	print("Program terminated by user.")
	exit()
# exit()

# print('Task started.')

import os
import sys

# print(sys.argv)
# print(len(sys.argv))
# print(os.getcwd())
# print('Separator')

for item in sys.argv[1:]:
	if item == '-s' or item == '--subfolder':
		subfolder = True
	elif item == '-d' or item == '--dryrun':
		dryrun = True
	elif item == '-sd':
		subfolder = True
		dryrun = True
	else:
		target = item

if not 'target' in locals():
	target = os.getcwd()
if not 'subfolder' in locals():
	subfolder = False
if not 'dryrun' in locals():
	dryrun = False

# print(subfolder)
# print(target)
# print(os.getenv("HOME"))
if target == os.getenv("HOME"):
	print('This program is prohibited to be run in home folder. \nProgram will now exit. Modify program to override.')
	exit()

charlist = [' ', '\\', '[', ']', '(', ')', '{', '}', '\'', '!', '+', '-', '~']
trans1 = ''.join(charlist)
trans2 = '_' * len(charlist)
transdict = ''.maketrans(trans1, trans2)
# print(trans1)
# print(trans2)
# print(transdict)
# exit()

# print('Checkpoint 1')
iteration = 1
count = 1
while count > 0:
	print(f'Iteration {iteration}')
	for folder, subfolders, files in os.walk(target):
		# print('\nFolder is :' + folder)
		# print('Checkpoint 2')
		if folder != target and subfolder == False:
			break
		# print('Checkpoint 3')

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

				countval = tempstring.count(".") - 1
				tempstring = tempstring.replace('.', '_', countval)
				tempstring = tempstring.replace('__','_')
				file_ext = tempstring.split('.')
				file_ext = '.' + file_ext[-1]
				# print(file_ext)
				# exit()

				www = 0
				year = len(tempstring.split('_'))
				for index,items in enumerate(tempstring.split('_')):
					if 'www' in items:
						www = index + 3
						break
				for index,items in enumerate(tempstring.split('_')):
					if items.isdigit() and index > www:
						year = index + 1
						break
				tempstring = tempstring.split('_')[www:year]
				tempstring = '_'.join(tempstring) + file_ext
				print(tempstring)
				# exit()


				postmod = os.path.join(folder, tempstring)
				# print(postmod)
				cmd = 'mv "' + premod + '" "' + postmod + '"'
				print(premod + ' --> ' + postmod)
				# print('\n' + cmd + '\n')
				if dryrun == False:
					os.system(cmd)

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
				tempstring = tempstring.replace('.','_')
				tempstring = tempstring.replace('__','_')


				www = 0
				year = len(tempstring.split('_'))
				for index,items in enumerate(tempstring.split('_')):
					if 'www' in items:
						www = index + 3
						break
				for index,items in enumerate(tempstring.split('_')):
					if items.isdigit() and index > www:
						year = index + 1
						break
				tempstring = tempstring.split('_')[www:year]
				tempstring = '_'.join(tempstring)
				# print(tempstring)
				# exit()

				postmod = os.path.join(folder, tempstring)
				# print(postmod)
				cmd = 'mv "' + premod + '" "' + postmod + '"'
				print(premod + ' --> ' + postmod)
				# print('\n' + cmd + '\n')
				if dryrun == False:
					os.system(cmd)
					count += 1
	count -= 1
	# print(count)
	iteration += 1

# print('Task completed.')
