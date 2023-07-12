from quadrado import*
lado=int(input('Digite o lado do quadrado: '))


quadrado1=Quadrado(lado)
quadrado1.mostra_area()

lado=int(input('Digite o novo lado do quadrado: '))
quadrado1.mudar_valor(lado)




