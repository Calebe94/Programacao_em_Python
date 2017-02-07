from urllib.request import urlopen
import json as simplejson
import os
response = urlopen("https://steampics-mckay.rhcloud.com/info?apps=227600&prettyprint=1")
data = simplejson.load(response)
"""Para Conseguir o nome do Executável precisamos da Seguinte sintaxe
    dicionário["apps"][<appID>]["config"]["launch"][<OS>]["executable"]
    <appID> é o appID do Jogo
    <OS>    0: Windows
            1: MacOS
            2: Linux
"""
print (data["apps"]["227600"]["config"]["launch"]["0"]["executable"])
