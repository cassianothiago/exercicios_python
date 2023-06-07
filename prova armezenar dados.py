lista=[]
while True:
    nome=(input('digite o nome do usuário ou zero para sair:  '))
    lista.append(nome)
    if nome=='0' or nome=='zero':
        print(lista)
        break
