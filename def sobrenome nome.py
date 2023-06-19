def invert(nome,sobrenome):
    nomeivert=sobrenome+','+nome
    return nomeivert
a=input('Nome: ')
b=input('sobrenome: ')
invertido=invert(a,b)
print('Olá',invertido)
