10.	#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
11.	#Altere o programa anterior para mostrar no final a soma dos números.

print('='*120)
a=int(input('digite o primeiro numero: '))
b=int(input('digite o segundo numero: '))
c=a
d=b
soma=0
print('='*120)

while a>b:
    print('o primeiro numero tem que ser menor que o segundo. digite novamente!')
    a=int(input('digite o primeiro numero: '))
    b=int(input('digite o segundo numero: '))
while a<(b-1):
    a=a+1
    print(a,end=(', '))
    soma=soma+a
print('')
print('='*120)
print('a soma dos numeros do intervalo entre {} e {} é {}'.format(c,d,soma))
print('='*120)
