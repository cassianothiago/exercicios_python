import secrets

a='a'
sorteio=[]
while a!='0':
    a=input('digite: ')
    sorteio.append(a)

sorteio.pop(-1)
print(sorteio)
