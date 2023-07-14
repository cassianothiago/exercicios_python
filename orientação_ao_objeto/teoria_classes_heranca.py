class Pessoa():
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cidade=cidade
        self.estado=estado

    def relatorio(self):
        print('Nome = ',self.nome)
        print('Idade = ',self.idade)
        print('endereco = ',self.endereco)
        print('cidade = ',self.cidade)
        print('Estado = ',self.estado)

class Aluno(Pessoa):
    def __init__(self, mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade=mensalidade
        print('----')
        print('Bem-vindo Aluno')
        super().relatorio()
        print('Mensalidade = ',self.mensalidade)
        print('-----')

class Professor(Pessoa):
    def __init__(self, salario, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario=salario
        print('-----')
        print('Bem-vindo Professor')
        super().relatorio()
        print('salario = ',self.salario)
        print('-----')
        