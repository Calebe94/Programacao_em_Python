#Export_XML
from xml.dom import minidom

my_file = minidom.Document()

root = my_file.createElement('installedGames')
my_file.appendChild(root)

steamID = my_file.createElement('steamID')
ID = my_file.createTextNode('Calebe94')
steamID.appendChild(ID)
root.appendChild(steamID)

vanityURL = my_file.createElement('vanityURL')
vanity = my_file.createTextNode('calebenovequatro')
vanityURL.appendChild(vanity)
root.appendChild(vanityURL)

games = my_file.createElement('games')
root.appendChild(games)

game = my_file.createElement('game')
games.appendChild(game)

appID = my_file.createElement('appID')
ID = my_file.createTextNode('APP_ID')
appID.appendChild(ID)
game.appendChild(appID)

name = my_file.createElement('name')
name_text = my_file.createTextNode('NAME')
name.appendChild(name_text)
game.appendChild(name)

logo = my_file.createElement('logo')
logo_url = my_file.createTextNode('URL')
logo.appendChild(logo_url)
game.appendChild(logo)

xml_str = my_file.toprettyxml(indent="  ")
with open("installedGames.xml", "w") as file:
    file.write(xml_str)
