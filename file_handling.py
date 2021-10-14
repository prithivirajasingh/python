# Open a file on same location:
with open('file.txt', 'r') as f:
print(f.read())

# Open a file on a different location:
with open('/home/prithivi/file.txt', 'r') as f:
  print(f.read())
  print(f.read(5))
  print(f.readline())
  print(f.readline())
  for x in f:
    print(x)

with open('/home/prithivi/file.txt', 'w+') as f:
  f.write("Woops! I have deleted the content!")

f.seek(offset, from_what)
# Offset: Number of positions to move forward 
# from_what: It defines point of reference. (Optional, Default: 0)
# 0: sets the reference point at the beginning of the file 
# 1: sets the reference point at the current file position 
# 2: sets the reference point at the end of the file 
print(f.tell()) # prints current position

with open('/home/prithivi/file.txt', 'rb') as f:
  print(f.readline().decode('utf-8'))

f = open("demofile2.txt", "a")
f.seek(10)
f.write("Now the file has more content!")
f.close()

import os
if os.path.exists("file.txt"):
  os.remove("file.txt") # same as os.unlink
  os.unlink('file.txt') # same as os.remove
else:
  print("The file does not exist")
os.rmdir("myfolder") # Note: You can only remove empty folders.
cmd = 'echo LINUX COMMAND HERE' # cmd = 'mv -n "' + premod + '" "' + postmod + '"'
os.system(cmd)
os.chdir('/tmp/')
for folder, subfolders, files in os.walk(target):
  pass
for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)

import shutil
shutil.copy('source_FILE', 'destination_FOLDER') # shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('source_FILE', 'destination_FILE')  # shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') # Copy and rename
shutil.copytree('source_FOLDER', 'destination_FOLDER')  # shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
shutil.move('source_FILE', 'destination_FOLDER') # shutil.move('C:\\bacon.txt', 'C:\\eggs')  
shutil.move('source_FILE', 'destination_FILE')  # shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') # Move and rename
# FileNotFoundError # If any folder before destination folder does not exist
shutil.rmtree(path)  # will remove the folder at path, and all files and folders it contains will also be deleted.

import zipfile
# Extract ZIP
os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
exampleZip.extractall()
exampleZip.extractall('C:\\ delicious')  # the code would extract the files from example.zip into a newly created C:\delicious folder
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()
# Compress ZIP
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


