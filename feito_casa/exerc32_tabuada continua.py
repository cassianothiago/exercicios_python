import os
print('Bem vindo a tabuada')
a=int(input('digite o numero para afetuar a tabuada ou zero para sair: '))
cont=0
while a!=0:
    while cont<10:
        cont=cont+1
        tab=a*cont
        print(a,'x',cont,'= ',tab)
    a=int(input('digite o numero para afetuar a tabuada ou zero para sair: '))
    cont = 0

os.system('pause')
