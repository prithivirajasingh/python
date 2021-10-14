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
