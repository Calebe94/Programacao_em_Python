import os

def scan_for_next_token(f):
    while True:
        byte = f.read(1)
        if byte == '':
            raise EOFError
        if not byte.isspace():
            return byte

def parse_quoted_token(f):
    ret = ''
    while True:
        byte = f.read(1)
        if byte == '':
            raise EOFError
        if byte == '"':
            return ret
        ret += byte

class AcfNode(dict):
    def __init__(self, f):
        while True:
            try:
                token_type = scan_for_next_token(f)
            except EOFError:
                return
            if token_type == '}':
                return
            if token_type != '"':
                raise TypeError('Error parsing ACF format - missing node name?')
            name = parse_quoted_token(f)

            token_type = scan_for_next_token(f)
            if token_type == '"':
                self[name] = parse_quoted_token(f)
            elif token_type == '{':
                self[name] = AcfNode(f)
            else:
                assert(False)

def parse_acf(filename):
    with open(filename, 'r') as f:
        return AcfNode(f)


WINE = "/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive_c/Program Files/Steam/"
publicID = "calebenovequatro"
LINUX="/home/calebe945/.steam/steam/"
def getInstalledGames():
    AUX = dict()
    client_wine = WINE + "steamapps/"
    client_linux = LINUX + "steamapps/"
    my_list ={"linux":client_linux,"windows":client_wine}
    
    for client in my_list:
        for file in os.listdir(my_list[client]):
            if file.endswith(".acf"):
                acf=parse_acf(my_list[client]+file)
                AUX.setdefault('name',[]).append({'name':acf['AppState']['name']})
                AUX.setdefault('appID',[]).append({'appID':acf['AppState']['appid']})
                header = "http://cdn.edgecast.steamstatic.com/steam/apps/%s/header.jpg"%acf['AppState']['appid']
                AUX.setdefault('logo',[]).append({'logo':header})
                AUX.setdefault('platform',[]).append({"platform":client})
    return AUX

newdict = dict()
newdict = getInstalledGames()

for count in range(0,len(newdict['name'])):
    print(newdict["name"][count]['name'])
    print(newdict['appID'][count]["appID"])
    print(newdict['logo'][count]['logo'])
    print(newdict['platform'][count]['platform'])
    print('\n')
