from urllib.request import urlopen

from collections import defaultdict
import xml.etree.ElementTree as ET

from xml.dom import minidom
from lxml import etree

import xml.sax
"""Aprendendo a Lidar com Dicionários para Fazer o Add-on"""
"""http://cdn.edgecast.steamstatic.com/steam/apps/appID/header.jpg?t=1466791207, Basta substituir o appID pelo appID do jogo e temos a imagem do jogo steam
https://github.com/SteamDatabase/SteamLinux JOGOS LINUX
"""

ALL_GAMES = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=xml'
LINUX_GAMES = 'https://raw.githubusercontent.com/SteamDatabase/SteamLinux/master/GAMES.json'
#data = urlopen('http://steamcommunity.com/id/calebenovequatro/games?tab=all&xml=1').read()
#root = etree.parse(data)
#tree = minidom.parseString(data)
#root = tree.getElementsByTagName('base:OBS_VALUE')

#xml.sax.parseString(data,)
#tree = ET.parse(data)
#tree = ET.parse(data)
#tree = ET.parse('/home/calebe945/Projetos/Programacao_em_Python/library_games.xml')
tree = ET.ElementTree(file=urlopen('http://steamcommunity.com/id/calebenovequatro/games?tab=all&xml=1'))
root = tree.getroot()

LIBRARY=dict()
count = 0
for game in root.iter('game'):
	LIBRARY.setdefault('GAMES',[]).append({'name':game.find('name').text,'appID':game.find('appID').text,'logo':game.find('logo').text})
	count=count+1

print(count)
#print(LINUX.keys())
for index in range(0,count):
	print(LIBRARY['GAMES'][index]['name'])
#for logo in range(1,count):
#	print(LIBRARY['GAMES'][logo]['logo'])
#print(LINUX.values())
#print(LINUX.items())

