class Funcionario():
    def __init__(self,nome,cpf,nascimento,endereco,telefone,email):
        self.nome=nome
        self.__cpf=cpf
        self.nascimento=nascimento
        self.__endereco=endereco
        self.telefone=telefone
        self.email=email
        
class Diretor(Funcionario):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
        
    def salario(self):
        self.salario=1000
        self.salario=self.salario+(self.salario*15)
        print('salario Base da categoria = R$ 1000.00\nSalario Base Diretor = R$ {:.2f}'.format(self.salario))
class Gerente(Diretor):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
        
    def salario(self):
        self.salario=1000
        self.salario=self.salario+(self.salario*10)
        print('Salario Base da categoria = R$ 1000.00\nSalario Base Gerente = R$ {:.2f} '.format(self.salario))

class Assistente(Gerente):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
    def salario(self):
        self.salario=1000    
        self.salario=self.salario+(self.salario*5)
        print('Salario Base da categoria = R$ 1000.00\nSalario Base Assistente = R$ {:.2f} '.format(self.salario))

class Estagiario(Assistente):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
    def salario(self):
        self.salario=1000
        print('Salario Base da categoria = R$ 1000.00\nSalario Base Estagiario = R$ {:.2f} '.format(self.salario+100))

class Imprimir(Funcionario):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
    def imprimir(self):
        print('Nome: ',self.nome)
        print('Nascimento: ',self.nascimento)
        print('Telefone:  ',self.telefone)
        print('Email: ',self.email)
        print(8*'\n')
        print('Assin:_____________________________________________')
        print('                         {}'.format(self.nome))
