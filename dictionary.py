from collections import defaultdict
"""Aprendendo a Lidar com Dicionários para Fazer o Add-on"""
LINUX=dict()
LINUX.setdefault('LINUX',[]).append({'name':'FEZ','appID':'21212'})
LINUX.setdefault('LINUX',[]).append({'name':'CASTLE','appID':'121212'})
LINUX.setdefault('WINE',[]).append({'name':'CASTLE','appID':'121212'})
print(LINUX.keys())
print(LINUX['LINUX'])
print(LINUX.values())
print(LINUX.items())
