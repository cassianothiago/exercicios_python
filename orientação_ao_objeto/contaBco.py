class Banco():
    def __init__(self,nome,saldo,cpf,senha):
        self.nome=nome
        self.__saldo=saldo
        self.__cpf=cpf
        self.__senha=senha

    def extrato(self,senha):
        if senha!=self.__senha:
            print('Senha inválida')
        else:
            print(self.__saldo)

    def depositar(self,dep):
        self.__saldo+=dep




    

