class Banco():
    def __init__(self,nome,saldo:float,cpf,senha):
        self.nome=nome
        self.__saldo=saldo
        self.__cpf=cpf
        self.__senha=senha

    def extrato(self,senha):
        if senha!=self.__senha:
            print('Senha inválida')
        else:
            print('saldo = ',self.__saldo)

    def depositar(self,dep):
        self.__saldo+=dep
        print('deposito efetuado com sucesso')

    def saque(self,senha,sacar):
        if senha!=self.__senha:
            print('senha inválida')
        else:
            self.__saldo-=sacar
            print('saldo= ',self.__saldo)
            
            

    

