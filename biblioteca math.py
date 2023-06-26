import math
import datetime
import time

x=3.5

math.ceil(x)
print(math.ceil(x))

y=-3
math.fabs(y)
print(math.fabs(y))

z=5
math.factorial(z)
print(math.factorial(z))

w=3.5
math.floor(w)
print(math.floor(w))

r=9
print(math.isqrt(r))

f=2
n=10
print(math.pow(f,n))


print(datetime.date.today())

import datetime as dt
print(dt.date.today())

print(dt.date.today().strftime(' hoje é %d/%m/%Y'))

print(dt.datetime.now())
print(dt.datetime.now().strftime('%d/%m/%Y%H:%M:%S'))

cont=0
j=time.perf_counter()
while cont<10:
    print(j)
    cont=cont+1
k=time.perf_counter()
print(k-j)

