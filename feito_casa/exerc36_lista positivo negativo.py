#Crie uma lista vazia, que será usado para receber 10 números com a estrutura FOR apresente ao final o total de números negativos e positivos digitados pelo usuário.

lista=[]
cont=0
cont2=0
for i in range(4):
    x=int(input('digite um nomero: '))
    lista.append(x)
    if x<0:
        cont=cont+1
    if x>0:
        cont2=cont2+1
print(cont)
print(cont2)
print(lista)

