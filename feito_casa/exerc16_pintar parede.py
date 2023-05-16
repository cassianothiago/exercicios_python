h=int(input('digite a altura da parede que vai ser pintada: '))
l=int(input('digite a largura da parede a ser pintada: '))
a=int(h*l)
latas=float(a/2)
print('='*120)

print('para uma parede de área de %d metros vai ser necessário %.2f latas de tintas'%(a,latas))
print('observação: sabe-se que um lata de tinta pinta 2m² de parede')
print('='*120)
