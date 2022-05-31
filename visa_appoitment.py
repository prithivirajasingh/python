#!/usr/bin/env python3
import pyautogui
import time
import random
import requests
import subprocess

encoding = 'utf-8'
alertUrl = 'https://api.telegram.org/bot5134072525:AAF7D7Vz-icJCLnfQpiLvzPLApVL0DWBEQg/sendMessage?chat_id=251799072&text='
infoUrl = 'https://api.telegram.org/bot5575037446:AAEJQXg03ILPfmBq9G4554whSkTt9938Vqw/sendMessage?chat_id=251799072&text='
run_count = 0

# exit(0)
while True:
    run_count += 1
    alertUrlNew = alertUrl + str(run_count)
    infoUrlNew = infoUrl + str(run_count)
    time.sleep(30)
    command = subprocess.Popen(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    window_name = ''
    for line in command.stdout:
        window_name = window_name + line.decode(encoding)
    # print(window_name)
    if not 'cgifederal.secure.force.com/scheduleappointment - Google Chrome' in window_name:
        print("Error: Window name doesn't match. Program will now exit with error code 1.")
        exit(2)
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
        screen_text = screen_text + line.rstrip(b'\n').decode(encoding)
    # print(screen_text)
    if '2022' in screen_text and 'November' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/scam.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        messageUrl = alertUrlNew + screen_text
        response = requests.get(messageUrl)
        exit(0)
    elif '2022' in screen_text and 'December' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/scam.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        messageUrl = alertUrlNew + screen_text
        response = requests.get(messageUrl)
        exit(0)
    elif 'January' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/scam.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        messageUrl = alertUrlNew + screen_text
        response = requests.get(messageUrl)
        exit(0)
    elif '2022' in screen_text or '2023' in screen_text:
        messageUrl = infoUrlNew + screen_text
        response = requests.get(messageUrl)
        temp = '/home/prithivi/visa/' + str(run_count) + '.png'
        command = subprocess.Popen(['mv', '/home/prithivi/visa/screenshot.png', temp],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    elif not 'no appoitments' in screen_text.lower() and not '202' in screen_text:
        command = subprocess.Popen(['ffplay', '/home/prithivi/visa/rain.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        messageUrl = alertUrlNew + screen_text
        response = requests.get(messageUrl)
        exit(1)
    # if 'maximum' in screen_text.lower():
    #     command = subprocess.Popen(['ffplay', '/home/prithivi/visa/rain.mp3'], stdout=subprocess.PIPE,
    #                                stderr=subprocess.STDOUT)
    #     exit(2)
    # if 'authorization' in screen_text.lower():
    #     command = subprocess.Popen(['ffplay', '/home/prithivi/visa/rain.mp3'], stdout=subprocess.PIPE,
    #                                stderr=subprocess.STDOUT)
    #     exit(3)
    # if 'human' in screen_text.lower():
    #     command = subprocess.Popen(['ffplay', '/home/prithivi/visa/rain.mp3'], stdout=subprocess.PIPE,
    #                                stderr=subprocess.STDOUT)
    #     exit(4)

    temp = random.randint(120, 240)
    print('Run count is: ' + str(run_count))
    print('Current time is: ' + time.strftime("%H:%M:%S", time.localtime()))
    print('Wait time is ' + str(temp) + ' seconds.')
    time.sleep(temp)
