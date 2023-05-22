#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
import os
num=int(input('digite um numero: '))
cont=0
cont2=0
while cont<=num:
    cont=+1
    div=num%cont
    if div==0:
        cont2=cont2+1

if cont2<=2:
    print('primo')
    os.system('pause')
    
else:
    print('não é primo')
    os.system('pause')
    


