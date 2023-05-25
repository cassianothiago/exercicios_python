#24.	Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados

print('='*120)
import os
print('='*120)
num=int(input('digite um numero: '))
a=num+1
cont=0
lista=[]
for x in range(1,a):
    print('x=' ,x)
    if num%x==0:
        cont=cont+1
        lista.append(x)
print('='*120)
if cont==2:
    print(' o numero {} é primo e seus divisores são: {}'.format(num,lista))
else:
    print('o numero {} não é primo e seus divisores são: {}'.format(num,lista))
print('='*120)
os.system('pause')
