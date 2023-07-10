class conta():
    def __init__(self,agencia,conta,nome,fone):
        self.agencia=agencia
        self.conta=conta
        self.nome=nome
        self.fone=fone
        self.saldo=0


    def deposito(self,valor):
        self.saldo+=valor
        

    def saque(self,valor):
        self.saldo-=valor


    def extrato(self):
        print('saldo = ',self.saldo)

        
