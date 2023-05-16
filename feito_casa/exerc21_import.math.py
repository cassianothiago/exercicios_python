import math #no caso para import só sqrt= from math import sqrt
num=float(input('digite um numero: '))
raiz=math.sqrt(num)
print('a raiz de {} é iqual a {}'.format(num, math.ceil(raiz)))
print('a raiz de {} é iqual a {}'.format(num, math.floor(raiz)))
print('a raiz de {} é iqual a {:.2f}'.format(num, raiz))
