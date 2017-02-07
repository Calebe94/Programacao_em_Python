from subprocess import Popen,PIPE
import os
import time
def pgrep(pattern):
    pid=""
    process = Popen(['pgrep',pattern],stdout=PIPE,stderr=PIPE)
    out = str(process.communicate()).split()
    
    if out is not None:
        for digit in out[0]:
            if digit.isdigit():
                pid=pid+digit
    return pid

#retorno = pgrep("steam")
#if retorno:
steam = pgrep("Steam.exe")
if(steam):
    os.system("wine /home/calebe945/PlayOnLinux\'s\ virtual\ drives/calebe945/drive_c/Program\ Files/Steam/Steam.exe -shutdown")
    while(pgrep("Steam.exe")):
        time.sleep(1)
#if pgrep("steam"):
#  print(retorno)
#else:
#   print("Sem Retorno")
    

