from sys import argv
script,filename = argv
txt = open(filename)
print("Aqui está o seu Arquivo: %r"%filename)
print (txt.read())
