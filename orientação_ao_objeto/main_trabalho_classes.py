from trabalho_classes import*
from os import system
print('-----')
print('Bem vindo ao cadastro do RH')
print('-----')
list_nome=[]
print('')
while True:
    try:
        nome=input('Digite o nome do funcionário\n0(zero) para colher assinatura e o fechar sistema\n= ')
        list_nome.append(nome)
        if nome=='0':
            system('cls')
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
        system('pause')
        system('cls')
        
    except:
        print('Dados invalidos!! Digite novamente')
        system('pause')
        system('cls')
    else:
    
        print('----')
        print('Cadastro do funcionario {} realizado com sucesso!!!!'.format(nome))
        print('----')
        system('pause')
        system('cls')
        print('Cargo que o funcionario {} irá exercer?..'.format(nome))
        print('-----')
        menu=input('Digite\n1 para Diretor\n2 para Gerente\n3 Assistente\n4 para estagiario\n:.')
        print('-----')
        if menu=='0':
            break
        if menu=='1':
            cadastro=Diretor(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('-----')
            print('cadastro salarial Efetuado com sucesso')
            print('-----')
            system('pause')
            system('cls')
        elif menu=='2':
            cadastro=Gerente(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('-----')
            print('cadastro salarial Efetuado com sucesso')
            print('-----')
            system('pause')
            system('cls')
        elif menu=='3':
            cadastro=Assistente(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('-----')
            print('cadastro salarial Efetuado com sucesso')
            print('-----')
            system('pause')
            system('cls')
        elif menu=='4':
            cadastro=Estagiario(nome,cpf,nascimento,endereco,tel,email)
            cadastro.salario()
            print('-----')
            print('cadastro salarial Efetuado com sucesso')
            print('-----')
            system('pause')
            system('cls')
        else:
            print('Opção inválida!!. Cadastro apagado!! Digite novamente.:')
            system('pause')
            system('cls')
            continue
while True:
    try:
        print('-----')
        imprimir=input('Digite o nome do funcionario para envio do documento:  ')
        system('cls')
    except ValueError:
        print('Digite apenas o nome do funcionario!!')
    except:
        print('Erro de relatorio')
    else:
        if imprimir in list_nome:
            encontrei=list_nome.index(imprimir)
            impr=Imprimir(list_nome[encontrei],cpf,nascimento,endereco,tel,email)
            print('Parabéns vc é o nosso novo funcionario')
            print('Assianr o documento e entregar no RH')
            print('OBS:. Qualquer divergecia de informação neste documento tratar pessoalmente com RH')
            print('------')
            impr.imprimir()
            print('Enviando para email do funcionario:/{}/........'.format(email))
            system('pause')
            print('email enviado com sucesso')
            system('pause')
            system('cls')
            break
        else:
            print('Funcionario não encontrado')
        
    