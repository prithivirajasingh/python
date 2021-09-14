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
if len(sys.argv) == 1:
	helpvar = 1

for item in sys.argv[1:]:
	if item == '-s' or item == '--subfolder':
		subfolder = True
	elif item == '-d' or item == '--dryrun':
		dryrun = True
	elif item == '-f' or item == '--force':
		forcerun = 1
	elif item == '-h' or item == '--help':
		helpvar = 1
	elif item[2:].isdigit():
		if '-f' in item:
			fcharlen = int(item[2:])
			# lcharlen = 0
			# forcerun = 1
		if '-l' in item:
			lcharlen = int(item[2:])
			# fcharlen = 0
			# forcerun = 1
	else:
		target = item

if not 'target' in locals():
	target = os.getcwd()
if not 'subfolder' in locals():
	subfolder = False
if not 'dryrun' in locals():
	dryrun = False
if not 'fcharlen' in locals():
	fcharlen = 0
if not 'lcharlen' in locals():
	lcharlen = 0
if not 'forcerun' in locals():
	forcerun = 0
if not 'helpvar' in locals():
	helpvar = 0

# print(subfolder)
# print(target)
# print(os.getenv("HOME"))
# print(fcharlen)
# print(lcharlen)
# exit()
if helpvar == 1:
	print('Renamechars is a program to rename files, written in python. \n')
	print('Use -s to include subfolders.')
	print("Use -f to force run the program on files that don't have trigger charlist.")
	print("Use -h for help.")
	print("Use -f## for first ## characters.")
	print("Use -l## for last ## characters.")
	print("Use -d for dryrun. \n")
	print("Usage example:")
	print("renamechars.py -h")
	print("renamechars.py -s -f -d")
	print("renamechars.py -f10")
	print("renamechars.py -l10")
	exit()

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
			if any(chars in item for chars in charlist) or forcerun == 1:
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
				if len(file_ext) > 1:
					file_ext = '.' + file_ext[-1]
					tempstring = tempstring.split('.')[:-1]
				else:
					file_ext = ''
					tempstring = tempstring.split('.')[0]
				# print(file_ext)
				# exit()

				www = 0
				tempstring = ''.join(tempstring)
				# print(tempstring)
				year = len(tempstring.split('_'))
				for index,items in enumerate(tempstring.split('_')):
					if 'www' in items:
						www = index + 3
						break
				for index,items in enumerate(tempstring.split('_')):
					if 'eason' in premod or 'EASON' in premod or 'S0' in premod or 's0' in premod or 'EP' in premod:
						# print(premod)
						# exit()
						break
					if items.isdigit() and index > www and len(items) == 4:
						year = index + 1
						break
				tempstring = tempstring.split('_')[www:year]
				tempstring = '_'.join(tempstring) 
				# print(tempstring)
				tempstring1 = ''
				tempstring2 = ''
				if fcharlen != 0 and fcharlen <= len(tempstring):
					tempstring1 = tempstring[0:fcharlen]
				if lcharlen != 0 and lcharlen <= len(tempstring):
					tempstring2 = tempstring[-lcharlen:]
				if tempstring1 != '' or tempstring2 != '':
					tempstring = tempstring1 + tempstring2
				# print(tempstring)
				# exit()
				tempstring = tempstring + file_ext
				# print(tempstring)
				# exit()


				postmod = os.path.join(folder, tempstring)
				# print(postmod)
				if postmod != premod:
					cmd = 'mv -n "' + premod + '" "' + postmod + '"'
					print(premod + ' --> ' + postmod)
					# print('\n' + cmd + '\n')
					if dryrun == False:
						os.system(cmd)

		for item in subfolders:
			premod = os.path.join(folder, item)
			# print(premod + '\n')
			if any(chars in item for chars in charlist) or forcerun == 1:
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
				tempstring = ''.join(tempstring)
				# print(tempstring)
				year = len(tempstring.split('_'))
				for index,items in enumerate(tempstring.split('_')):
					if 'www' in items:
						www = index + 3
						break
				for index,items in enumerate(tempstring.split('_')):
					if 'eason' in premod or 'EASON' in premod or 'S0' in premod or 's0' in premod or 'EP' in premod:
						# print(premod)
						# exit()
						break
					if items.isdigit() and index > www and len(items) == 4:
						year = index + 1
						break
				tempstring = tempstring.split('_')[www:year]
				tempstring = '_'.join(tempstring) 
				# print(tempstring)
				tempstring1 = ''
				tempstring2 = ''
				if fcharlen != 0 and fcharlen <= len(tempstring):
					tempstring1 = tempstring[0:fcharlen]
				if lcharlen != 0 and lcharlen <= len(tempstring):
					tempstring2 = tempstring[-lcharlen:]
				if tempstring1 != '' or tempstring2 != '':
					tempstring = tempstring1 + tempstring2
				# print(tempstring)
				# exit()

				postmod = os.path.join(folder, tempstring)
				# print(postmod)
				if postmod != premod:
					cmd = 'mv -n "' + premod + '" "' + postmod + '"'
					print(premod + ' --> ' + postmod)
					# print('\n' + cmd + '\n')
					if dryrun == False:
						os.system(cmd)
						count += 1
	count -= 1
	# print(count)
	iteration += 1

# print('Task completed.')
