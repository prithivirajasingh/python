import os
import pymsgbox
import time

#time.sleep(3)
win_title = os.popen('xdotool getactivewindow getwindowname').read()
print(win_title)
if '.JPG' in win_title or '.jpg' in win_title:
    image_title = win_title.split('.JPG')[0] + '.JPG'
    # print(image_title)

    src_dir = '/media/prithivi/E_Data/Yosemite_25-Jun-2021/'
    dest_dir = '/media/prithivi/E_Data/Python_copy/'

    cmd = 'cp ' + src_dir + image_title + ' ' + dest_dir
    print(cmd)
    os.system(cmd)
else:
    pymsgbox.alert('Not an image', 'Python')
    exit()
