import os
path="/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive_c/Program Files/Steam/"
#path="/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive/Program Files/Steam"

if os.path.isdir(path) is True:
    print("É um Diretório!")
else:
    print("Não é um Diretório!")

if os.path.exists(path) is True:
    print("Diretório Existe")
else:
    print("Diretório Não Existe")
