def cadastro():
    name=input('digite o nome: ')
    age=input('digite a idade: ')
    return name,age
print('iniciando cadastro')
nome,idade=cadastro()
print('cadastro realizado')
print('seu nome é',nome,'sua idade é',idade)