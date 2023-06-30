import matplotlib.pyplot as plt
import math
lista=[]
x=int(input('digite x: '))
for i in range(x):
    y=math.sqrt(i)
    lista.append(y)
plt.plot(i,lista,'y')
plt.grid()
plt.show()
