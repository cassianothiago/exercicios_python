16.#	A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

print('='*120)
print('F(n+1)=Fn+Fn-1, n>=2 (formula da sequência de Fibonacci)')
n=int(input('digite o valor de n para a sequencia de Fibonacci. (n tem que ser maior ou iqual a 2): '))
cont=0
fb=1
fb1=1
while n<2:
    n=int(input('valor de n tem que ser maior ou iqual a 2. Digite novamente: '))
if n==2:
    print('{}, {}'.format(1,2))
elif n==3:
    print('{}, {}, {}'.format(1,2,3))
else:
    while cont<n:
        cont=cont+1
        a=fb+fb1
        fb1=fb
        fb=a
        print(a)
print('='*120)
