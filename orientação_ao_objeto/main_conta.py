from conta import*
print('-----')

agencia=input('digite a sua agencia: ')
rconta=input('digite sua conta: ')
nome=input('digite seu nome: ')
fone=input('digite seu fone: ')
print('-----')

conta1 = conta(agencia,rconta,nome,fone)
while True:
    a=input('digite 1 para deposito\ndigite 2 para sacar\ndigite 3 para extrato\nzero para sair\n')
    if a=='1':
        try:
            depositar=float(input('digite o valor depositado = '))
            conta1.deposito(depositar)
            print('saldo = ',conta1.saldo)
            print('----')
        except ValueError:
            print('valor invalido')
        except:
            print('erro')
    if a=='2':
        try:
            sacar=int(input('digite o valor para saque = '))
            conta1.saque(sacar)
            print('saldo = ',conta1.saldo)
            print('----')
        except ValueError:
            print('valor para saque invalido')
        except:
            print('erro')
    if a=='3':
        conta1.extrato()
    if a=='0':
        break
    if a!='0' and a!='1' and a!='2' and a!='3':
        print('----')
        print('erro! digite novamente')
print(agencia)
print(rconta)
print(nome)
print(fone)
print('saldo = ',conta1.saldo)