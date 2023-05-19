12.	#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada

print('='*120)
cont=0
mult=int(input('digite o numero que deseja ver a tabuada: '))

while cont<10:
    cont=cont+1
    tab=mult*cont
    print('{} X {} = {}'.format(mult,cont,tab))
print('='*120)
