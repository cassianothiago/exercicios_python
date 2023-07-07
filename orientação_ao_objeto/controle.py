class Controle():
    def __init__(self,cor,altura,largura,botao):
        self.cor=cor
        self.altura=altura
        self.largura=largura
        self.botao=botao
    def cores(self,cores):
        self.cor=cores
        print('sua nova cor é',self.cor)
    def tamanho_altura(self,altura):
        self.altura=altura
        print('sua nova altura é',self.altura)
    def tamanho_largura(self,largura):
        self.largura=largura
        print('sua nova largura é',self.largura)  
    def quant_botoes(self,botao):
        self.botao=botao
        print('quantidade de botões é',self.botao)

    def mudar_canal(self,mudar):
        self.mudar=mudar
        print('ligar no canal:',self.mudar)
