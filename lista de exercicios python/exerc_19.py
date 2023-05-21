#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
print('='*120)
soma=0
lista=[]

while True:
    num=int(input('digite os numeros que deseja somar e digite zero para ver o resultado da soma: '))
    soma=soma+num
    lista.append(num)
    if num==0:
        lista.remove(0)
        print(lista)
        print('a soma dos numeros digitados é {} o menor valor é {} e o maior é {}'.format(soma,min(lista),max(lista)))
        break
print('='*120)
