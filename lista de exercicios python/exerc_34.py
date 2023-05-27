'''34.	O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''

import os
print('='*120)
lista=[]
soma=0
cont=0
while True:
    temp=(input('digite as temperaturas e digite "X" para sair: '))
    cont=cont+1
    if temp=='x' or temp=='X':
        break
    temp=float(temp)
    lista.append(temp)
    soma=soma+temp
    media=soma/cont
if lista!=0:
    print('a menor temperatura= ',min(lista))
    print('a maior temperaturra= ',max(lista))
    print('a media das temperaturas= ',media)
print('='*120)
os.system('pause')
