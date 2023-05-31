codigo=5
lista=[]
lista2=[]
for i in range(codigo):
    passeio=int(input('quantos veiculos de passeio da cidade de código {}: '.format(i+1)))
    acidentes=int(input('numero de acidentes da cidade do código {}: '.format(i+1)))
    soma=soma+acidentes
print('media das cidades juntas = ',soma/5)


