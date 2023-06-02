import os
print('='*120)
listainpar=[]
listapar=[]
contim=0
contpar=0

for i in range(10):
    num=int(input('digite o {}º numero: '.format(i+1)))
    if (i)%2!=0:
        contim=contim+1
        listainpar.append(num)
        
    else:
        contpar=contpar+1
        listapar.append(num)
print(listainpar,' Qtde = ',contim)
print(listapar,' Qtde = ',contpar)
print('')
print('='*120)
os.system('pause')