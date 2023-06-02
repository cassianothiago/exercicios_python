import os
print('='*120)
lista_temp=[]
lista_mes=[]
lista_ano=[]
soma=0
cont=0
while True:
    temp=(input('digite as temperaturas e digite "X" para sair: '))
    if temp=='x' or temp=='X':
        break
    mes=int(input('digite o mes que essa temp ocorreu: '))
    
    if mes<1 or mes>12:
        print('mês invalido. Favor difitar novamente!')
        while mes<1 or mes>12:
            mes=int(input('digite o mes que essa temp ocorreu: '))
    
    ano=int(input('digite o ano que ocorreu: '))
    cont=cont+1
   
    temp=float(temp)
    lista_temp.append(temp)
    lista_mes.append(mes)
    lista_ano.append(ano)
    soma=soma+temp
    media=soma/cont
if lista_temp!=0:
    print('a menor temperatura= ',min(lista_temp))
    x=min(lista_temp)
    z=lista_temp.index(x)
    print('o mes que ocorreu: ',lista_mes[z])
    print('o ano que ocorreu',lista_ano[z])
    print('a maior temperaturra= ',max(lista_temp))
    y=max(lista_temp)
    w=lista_temp.index(y)
    print('o mes que ocorreu: ',lista_mes[w])
    print('o ano que ocorreu',lista_ano[w])
    print('a media das temperaturas= ',media)
print('='*120)
os.system('pause')