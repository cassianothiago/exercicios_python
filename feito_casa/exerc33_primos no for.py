print('='*120)
num=int(input('digite um numero: '))
cont=0
for x in range(2,num):
    print('x=' ,x)
    if num%x==0:
        cont=cont+1
print('='*120)
if cont==0:
    print('primo')
else:
    print('não é primo')
print('='*120)
