#!/usr/bin/env python3

import subprocess as sub
import time

encoding = 'utf-8'
lookoutGeometry = '272x269'

while True:
    command = ['xdotool', 'search', 'TeamViewer']
    winId = sub.Popen(command, stdout=sub.PIPE, stderr=sub.STDOUT)
    winIdOut = []
    for line in winId.stdout:
        winIdOut.append(line.rstrip(b'\n').decode(encoding))

    # print(winIdOut)

    for item in winIdOut[1:]:

        command = ['xwininfo', '-id', item]
        # print(command)
        winInfo = sub.Popen(command, stdout = sub.PIPE, stderr=sub.STDOUT)
        winInfoOut = []
        for line in winInfo.stdout:
            winInfoOut.append(line.rstrip(b'\n').decode(encoding))
            if lookoutGeometry in winInfoOut[-1]:
                axisList = winInfoOut[-2].strip().split(' ')[2].split('+')
                # print(axisList)
                xaxis = str(int(float(axisList[1]) * 1.015))
                # xaxis = '10'
                yaxis = str(int(float(axisList[2]) * 1.95))
                # yaxis = '40'
                command = ['xdotool', 'mousemove', xaxis, yaxis, 'click', '1']
                # print(command)
                mouseCommand = sub.Popen(command, stdout=sub.PIPE, stderr=sub.STDOUT)
                # exit()
            # print(line.rstrip(b'\n').decode(encoding))
        # print('\n'.join(winInfoOut))
    time.sleep(10)


