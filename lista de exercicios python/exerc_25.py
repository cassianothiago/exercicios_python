#25.	Faça um programa que calcule o mostre a média aritmética de N notas

import os
print('='*120)
print('bem vindo ao calculo da média')
print('='*120)
provas=int(input('digite quantas provas foram feitas: '))
cont=0
soma=0
lista=[]
while cont<provas:
    notas=float(input('digite sua nota na prova: '))
    cont=cont+1
    lista.append(notas)
    soma=soma+notas
    media=soma/provas
print('='*120)
print('As suas notas nas provas foram {} e a média é iqual a {}'.format(lista,media))
print('='*120)
os.system('pause')
