import xml.etree.ElementTree as ET
tree = ET.parse('/home/calebe94/Projetos/Programacao_em_Python/country_data.xml')
root = tree.getroot()
#for child in root:
#     print(child.tag, child.attrib)
#deu certo
for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)
