from subprocess import Popen, PIPE
#import os
import os
pid=os.fork()        
if pid==0:
    process = Popen(['steam','-applaunch','200900','&'], stdout=PIPE, stderr=PIPE)
#    os.system(executable)
#    exit()
#process = Popen(['pgrep','-lf','kodi'], stdout=PIPE, stderr=PIPE)
#process = Popen(['steam','-applaunch','200900','&'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
#pid = process.pid
#print(stdout)
#print(stderr)

#os.system("steam -applaunch 200900 -silent &")
#print(pid)
