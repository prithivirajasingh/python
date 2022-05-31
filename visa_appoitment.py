#!/usr/bin/env python3
import pyautogui
import time
import random
import subprocess

encoding = 'utf-8'

while True:
    time.sleep(10)
    command = subprocess.Popen(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    window_name = ''
    for line in command.stdout:
        window_name = window_name + line.decode(encoding)
    # print(window_name)
    if not 'cgifederal.secure.force.com/scheduleappointment - Google Chrome' in window_name:
        print("Error: Window name doesn't match. Program will now exit with error code 1.")
        exit(1)
    pyautogui.press('f5')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    command = subprocess.Popen(['xfce4-screenshooter', '-f', '-s', '/home/prithivi/visa/screenshot.png'],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # screen_image = ''
    # for line in command.stdout:
    #     screen_image = screen_image + line.decode(encoding)
    # print(screen_image)
    time.sleep(2)
    command = subprocess.Popen(['tesseract', '--dpi', '96', '/home/prithivi/visa/screenshot.png', '-'],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    screen_text = ''
    for line in command.stdout:
        screen_text = screen_text + line.decode(encoding)
    print(screen_text)
    if '2022' in screen_text and 'November' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/scam.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        exit(0)
    if '2022' in screen_text and 'December' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/scam.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        exit(0)
    if 'January' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/scam.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        exit(0)
    if 'maximum' in screen_text.lower():
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/rain.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        exit(2)
    if 'authorization' in screen_text.lower():
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/rain.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        exit(3)
    time.sleep(random.randint(1, 4) * 60)
