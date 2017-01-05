#from sys import argv
#script,filename = argv

txt = open("teste_lendo_escrevendo_python.txt",'w')
txt.write('Isso é tudo Pessoal!')
txt.truncate()
txt.close()
txt = open("teste_lendo_escrevendo_python.txt",'r')
print(txt.read())
