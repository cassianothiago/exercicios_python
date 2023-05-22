#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num=int(input('digite um numero: '))
cont=0
cont2=0
while cont<=num or cont<2:
    cont=+1
    div=num%cont
    if div==0:
        cont2=cont2+1

    if cont<=2:
        print('primo')
    else:
        print('não é primo')
    

