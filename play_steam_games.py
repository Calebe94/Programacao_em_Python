import webbrowser
print("Iniciando Cave Story+")
# Esse pode ser usada para executar jogos linux
webbrowser.open('steam://rungameid/227600')


#from subprocess import Popen, PIPE
import os

#process = Popen(['steam','-applaunch','200900','-silent'], stdout=PIPE, stderr=PIPE)
#stdout, stderr = process.communicate()
#pid = process.pid

#pode ser usado para executar jogos Wine
os.system("steam -applaunch 200900 -silent &")
#print(pid)
print("Cave Story+ terminou!")
