from contaBco import*
from os import system

print('-----')
print('abertura de conta')
nome=input('Digite seu nome: ')
saldo=0
cpf=int(input('digite seu cpf:  '))
senha=int(input('Digite uma senha de quatros numeros: '))
print('----')
print('conta cadastrada')
print('---')
contabco=Banco(nome,saldo,cpf,senha)
system('pause')
system('cls')
while True:
    print('-----')
    menu=int(input('1 para deposito\n2 para extrato\n3 para saque\nzero para encerrar: '))
    print('-----')
    if menu==1:
        print('Depositar\n-----')
        dep=float(input('Valor do deposito = '))
        contabco.depositar(dep)
        system('pause')
        system('cls')
    elif menu==2:
        print('Extrato\n-----')
        digt_senha=int(input('Digite sua senha: '))
        contabco.extrato(digt_senha)
        system('pause')
        system('cls')
    elif menu==3:
        print('Sacar\n-----')
        digt_senha=int(input('Digite sua senha: '))
        dinheiro=float(input('Valor do saque = '))
        contabco.saque(digt_senha,dinheiro)
        system('pause')
        system('cls')
    elif menu==0:
        break
