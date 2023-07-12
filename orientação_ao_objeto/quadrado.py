class Quadrado():
    def __init__(self,tamanho_lado):
        self.tamanho_lado=tamanho_lado
        self.area=self.tamanho_lado**2

    def mostra_area(self):
        print(self.area)
        
    def mudar_valor(self,tamanho_lado):
        self.tamanho_lado=tamanho_lado
        self.area=tamanho_lado**2
        print(self.area)