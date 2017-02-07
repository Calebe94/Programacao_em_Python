from collections import defaultdict
"""Aprendendo a Lidar com Dicionários para Fazer o Add-on"""
#LIBRARY.setdefault('GAMES',[]).append({'name':game.find('name').text,'appID':game.find('appID').text,'logo':game.find('logo').text})
def getGames():
    DICT = {"name":"CASTLE","appID":"22121"}
    return DICT
LINUX=dict()
LINUX.setdefault('LINUX',[]).append({'name':'FEZ','appID':'21212'})
LINUX.setdefault('LINUX',[]).append({'name':'CASTLE','appID':'121212'})
LINUX.setdefault('WINE',[]).append({'name':'CASTLE','appID':'121212'})
LINUX.setdefault('OWNED',[])
print(LINUX.keys())
print(LINUX['LINUX'])
print(LINUX.values())
print(LINUX.items())
LINUX['OWNED'] = getGames()
print(LINUX)
