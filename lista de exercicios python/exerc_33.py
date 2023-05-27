'''33.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
a.	Fatorial de: 5
b.	5! =  5 . 4 . 3 . 2 . 1 = 120'''

print('='*120)
a=int(input('a.  Fatorial de: '))
lista=[]
b=1
for x in range(a):
    b=(x+1)*b
    c=a-x
    lista.append(c)
print('b. ',a,'! = ',' . '.join(map(str,lista)),' = ',b)
print('='*120)
