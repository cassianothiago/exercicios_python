a=5
soma=0
for x in range(a):
    print('digite o ',x+1,'º numero',end=(' '))
    num=int(input(':'))
    soma=soma+num
media=soma/5
print('soma=',soma,'media=',media)
