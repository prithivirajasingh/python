import subprocess as sub

encoding = 'utf-8'
cmd = sub.Popen( ['ls', '-a', '-l'], stdout = sub.PIPE, stderr=sub.STDOUT)
for line in cmd.stdout:
    print(line.rstrip(b'\n').decode(encoding))

