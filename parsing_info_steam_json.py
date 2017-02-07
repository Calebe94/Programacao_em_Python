import json
from pprint import pprint

with open('info_cave.acf') as data_file:
    data = json.load(data_file)
#print(data['apps']['200900']['common']['oslist'])
#print(data['apps']['200900']['config']['launch']['0']['executable'])
pprint(data['apps']['200900']['depots'])
