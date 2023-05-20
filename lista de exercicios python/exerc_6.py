"""Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro."""
import os
print('='*120)
cont=0
contl=0
while cont<20:
    cont=cont+1
    print(cont,'\n')
print('='*120)
while contl<20:
    contl=contl+1
    print(contl,end=', ')
print('')
print('='*120)
os.system('pause')
