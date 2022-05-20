import subprocess as sub

encoding = 'utf-8'

winId = sub.Popen( ['xdotool', 'getactivewindow'], stdout = sub.PIPE, stderr=sub.STDOUT)
winIdOut = []
for line in winId.stdout:
    winIdOut.append(line.rstrip(b'\n').decode(encoding))

print(winIdOut)
command = ['xwininfo', '-id', winIdOut[0]]
print(command)

winInfo = sub.Popen(command, stdout = sub.PIPE, stderr=sub.STDOUT)
winInfoOut = []
for line in winInfo.stdout:
    winInfoOut.append(line.rstrip(b'\n').decode(encoding))
    # print(line.rstrip(b'\n').decode(encoding))

print('\n'.join(winInfoOut))


