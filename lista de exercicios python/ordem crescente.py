print('='*120)
a=int(input('digite o primeiro numero: '))
b=int(input('digite o segundo numero: '))
c=int(input('digite o terceiro numero: '))
print('='*120)

if a<b and a<c and b<c:
    print('ordem decrescente: {}-{}-{}'.format(a,b,c))
elif b<a and b<c and a<c:
    print('ordem decrescente: {}-{}-{}'.format(b,a,c))
elif c<a and c<b and b<a:
    print('ordem decrescente: {}-{}-{}'.format(c,b,a))
elif c<a and a<b and c<b:
    print('ordem decrescente: {}-{}-{}'.format(c,a,b))
elif a<b and a<c and c<b:
    print('ordem decrescente: {}-{}-{}'.format(b,c,a))
else:
    print('ordem decrescente: {}-{}-{}'.format(a,c,b))
print('='*120)

