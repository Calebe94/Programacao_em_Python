import os
from subprocess import Popen, PIPE
STEAM_WINE_EXECUTABLE = "/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive_c/Program Files/Steam/Steam.exe"
CREATIVERSE = "280790"

process = Popen(['wine',STEAM_WINE_EXECUTABLE,'-applaunch',CREATIVERSE,'-silent'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
#sem o Pid o código termina deixando a steam aberta
pid = process.pid
#oi = "wine %s -applaunch %s"%(STEAM_WINE_EXECUTABLE,CREATIVERSE)
#os.system(oi)
