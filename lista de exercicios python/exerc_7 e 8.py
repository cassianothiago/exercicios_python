"""	Faça um programa que leia 5 números e informe o maior número."""

print('='*120)
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=int(input('digite um numero: '))
d=int(input('digite um numero: '))
e=int(input('digite um numero: '))
print('='*120)
if a>b and a>c and a>d and a>e:
    print('{} é o maior numero'.format(a))
elif b>a and b>c and b>d and b>e:
    print('{} é o maior numero'.format(b))
elif c>a and c>b and c>d and c>e:
    print('{} é o maior numero'.format(c))
elif d>a and d>b and d>c and d>e:
    print('{} é o maior numero'.format(d))
else:
    print('{} é o maior numero'.format(e))
print('='*120)
soma=(a+b+c+d+e)
media=float(a+b+c+d+e)/5
print('a soma dos números é {} é a media é {:.2f}'.format(soma,media))
print('='*120)
