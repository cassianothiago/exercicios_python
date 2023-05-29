#Crie uma lista com com 10 números e exiba a soma dos números no terminal utilizando a estrutura de repetição FOR. 

lista=[]
soma=0
for i in range(10):
    lista.append(int(input('digite: ')))
    soma=i+soma
for item in lista:
    print(item)
print(soma)
