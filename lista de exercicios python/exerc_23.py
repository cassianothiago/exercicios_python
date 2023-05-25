#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

import os
print('='*120)
num=int(input('digite um numero: '))
cont=0
lista=[]
for x in range(2,num):
    print('x=' ,x)
    if num%x==0:
        cont=cont+1
        lista.append(x)
print('='*120)
if cont==0:
    print('primo')
else:
    print('não é primo e seus divisores são: ',lista)
print('='*120)
os.system('pause')
