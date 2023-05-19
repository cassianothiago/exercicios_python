15.	#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares

print('='*120)
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=int(input('digite um numero: '))
d=int(input('digite um numero: '))
e=int(input('digite um numero: '))
f=int(input('digite um numero: '))
g=int(input('digite um numero: '))
h=int(input('digite um numero: '))
i=int(input('digite um numero: '))
j=int(input('digite um numero: '))
lista=[]
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
lista.append(f)
lista.append(g)
lista.append(h)
lista.append(i)
lista.append(j)
print(lista)
cont=0
while cont<10:
    cont=cont+1
    if lista[cont]%2==0:
        print(lista[cont])
