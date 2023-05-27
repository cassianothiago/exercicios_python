
print('quando quiser sair digite "X"')
lista=[]
while True:
    a=(input('digite o valor: '))
    if a=='x':
        break
    a=int(a)
    lista.append(a)
print('='*120)
if len(lista)!=0:
    print('o menor valor: ',min(lista))
    print('o maior valor: ',max(lista))
    print('soma dos valores digitados: ',sum(lista))
    print('todos os valores digitados: ',lista)
print('='*120)
