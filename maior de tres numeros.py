print('='*120)
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=int(input('digite um numero: '))
print('='*120)
if a>b and a>c: 
    print('{} é o maior numero'.format(a))
elif b>a and b>c:
    print('{} é o maior numero'.format(b))
else:
    print('{} é o maior numero'.format(c))
print('='*120)
