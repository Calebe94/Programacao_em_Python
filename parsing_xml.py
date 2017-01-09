import xml.etree.ElementTree as ET
tree = ET.parse('/home/calebe945/Projetos/Programacao_em_Python/library_games.xml')
root = tree.getroot()
for child in root:
     print(child.tag)
count = 0
for game in root.iter('game'):
	print(game.find('name').text,game.find('appID').text)
	count=count+1

print(count)
#deu certo
#print(root.tag)
#print(root.attrib)
