wine="wine"
executable="Steam.exe"
argument1="-applaunch"
gameID="280790"
argument2="-silent"

def path2UNIX(path):
    aux=str()
    for index in range(0,len(path)):
        if path[index] == '\'':
            aux=aux+'\\'
        elif path[index] == ' ':
            aux=aux+'\\'
        aux=aux+path[index]
        index=index+1
    return aux
path_steam="/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive_c/Program Files/Steam/"
print("String Lida pelo KODI:%s"%path_steam)    
print("String Manipulada:%s"%path2UNIX(path_steam))
path_manipulada = "/home/calebe945/PlayOnLinux\'s\ virtual\ drives/calebe945/drive_c/Program\ Files/Steam/"
