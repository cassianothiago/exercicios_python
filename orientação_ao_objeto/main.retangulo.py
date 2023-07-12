from retangulo import*

base_ret=float(input('Digite a base do rentangulo: '))
altura_ret=float(input('digite a altura do rentagulo: '))

retangulo1=Retangulo(base_ret,altura_ret)
retangulo1.area_retangulo()
retangulo1.rodape()

nova_base1=float(input('Nova base = '))
nova_altura1=float(input('Nova altura = '))
retangulo1.novo_retangulo(nova_base1,nova_altura1)
retangulo1.rodape()