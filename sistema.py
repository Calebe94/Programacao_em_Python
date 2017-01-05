from subprocess import Popen, PIPE
import os
process = Popen(['steam','-applaunch','200900'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
pid = process.pid
print(pid)
