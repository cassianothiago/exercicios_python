#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num=int(input('digite um numero: '))
cont=0
while cont<=num:
    cont=+1
    div=num%cont
    if div<=num or cont<2:
        print(div)
        
        break
    else:
        print('não é primo')
        break

