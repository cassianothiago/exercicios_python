class Retangulo():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        self.area=self.base*self.altura
        self.perimetro=2*(self.base+self.altura)

    def area_retangulo(self):
        print(self.area)
        print(self.perimetro)
    
    def novo_retangulo(self,nova_base,nova_altura):
        self.base=nova_base
        self.altura=nova_altura
        self.area=self.base*self.altura
        self.perimetro=2*(self.base+self.altura)
        

        print(self.area)
        print(self.perimetro)

    def rodape(self):
        self.rodapes=(self.area*15/100)
        print(self.rodapes)