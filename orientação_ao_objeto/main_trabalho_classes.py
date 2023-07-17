from trabalho_classes import*
from os import system
print('-----')
print('Bem vindo ao cadastro do RH')
print('-----')
while True:
    try:
        nome=input('Digite o nome do funcionário ou 0(zero) para sair = ')
        if nome=='0':
            break
        cpf=int(input('Digite seu CPF = '))
        nascimento=input('Digite seu nascimento = ')
        endereco=input('Digite seu endereço = ')
        tel=int(input('Digite seu número de telefone = '))
        email=input('Digite seu email = ')
        system('pause')
        system('cls')
    except ValueError:
        print('Dados invalidos!! Digite novamente ')
        
    except:
        print('Dados invalidos!! Digite novamente')
    else:
    
        print('----')
        print('Cadastro do funcionario {} realizado com sucesso!!!!'.format(nome))
        print('----')
        system('pause')
        system('cls')
        print('Cargo que o funcionario {} irá exercer?..'.format(nome))
        print('-----')
        menu=input('Digite\n1 para Diretor\n2 para Gerente\n3 Assistente\n4 para estagiario\nE 0(zero) para encerrar\n:.')
        print('-----')
        if menu=='0':
            break
        if menu=='1':
            cadastro=Diretor(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('cadastro Efetuado com sucesso')
            system('pause')
            system('cls')
        elif menu=='2':
            cadastro=Gerente(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('cadastro Efetuado com sucesso')
            system('pause')
            system('cls')
        elif menu=='3':
            cadastro=Assistente(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('cadastro Efetuado com sucesso')
            system('pause')
            system('cls')
        elif menu=='4':
            cadastro=Estagiario(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('cadastro Efetuado com sucesso')
            system('pause')
            system('cls')
        else:
            print('Opção inválida!!. Cadastro apagado!! Digite novamente.:')
            system('pause')
            system('cls')

    