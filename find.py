from subprocess import Popen,PIPE
import os

process = Popen(["find",".","-name","Steam.exe"],stdout=PIPE,stderr=PIPE)
out = str(process.communicate()).split()
print(out[0]+out[1])
