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
        print('salario Base funcionario = R$ 1000\nSalario Base Diretor = ',self.salario)
class Gerente(Diretor):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
        
    def salario(self):
        self.salario=1000
        self.salario=self.salario+(self.salario*10)
        print('Salario Base funcionario = R$ 1000\nSalario Base Gerente = ',self.salario)

class Assistente(Gerente):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
    def salario(self):
        self.salario=1000    
        self.salario=self.salario+(self.salario*5)
        print('Salario Base funcionario = R$ 1000\nSalario Base Assistente = ',self.salario)

class Estagiario(Assistente):
    def __init__(self, nome, cpf, nascimento, endereco, telefone, email):
        super().__init__(nome, cpf, nascimento, endereco, telefone, email)
    def salario(self):
        self.salario=1000
        print('Salario Base funcionario = R$ 1000\nSalario Base Estagiario = ',self.salario+100)


