from Bola import*

origem_cor='Branca'
origem_circunferencia=10
origem_material='lona'
print('-----')


bola1=Bola(origem_cor,origem_circunferencia,origem_material)
print('original = ',bola1.cor)
print('original = ',bola1.circunferencia)
print('original = ',bola1.material)
print('-----')

mudar_cor=input('Digite a nova cor: ')
mudar_circunferencia=(input('Digite a nova circunferencia: '))
mudar_material=(input('Digite o novo material: '))
print('Alteração efetuada com sucesso')
menu=input('Deseja imprimir digite 1 ou zero para encerrar: ')
if menu=='1':
    print('-----')
    bola1.mudar(mudar_cor,mudar_circunferencia,mudar_material)
    print('nova cor = ',bola1.cor)
    print('nova circunferencia = ',bola1.circunferencia)
    print('novo material = ',bola1.material)
    print('-----')
if menu=='0':
    print('encerrado')

    
