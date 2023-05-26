
print('quando quiser sair digite "X"')
lista=[]
while True:
    a=(input('digite o valor: '))
    if a=='x':
        break
    a=int(a)
    lista.append(a)
print(min(lista))
print(max(lista))
print(sum(lista))
print(lista)
