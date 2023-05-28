'''37.	Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
a.	Montar a tabuada de: 5
b.	Começar por: 4
c.	Terminar em: 7
d.	
e.	Vou montar a tabuada de 5 começando em 4 e terminando em 7:
f.	5 X 4 = 20
g.	5 X 5 = 25
h.	5 X 6 = 30
i.	5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''

import os
print('='*120)
print('              -------------tabuada----------------          ')
print('='*120)
tab=int(input('Montar a tabuada do número: '))
com=int(input('Comerçar por: '))
ter=int(input('Terminar em: '))
print('='*120)
while com>ter:
    print('"Comerçar por" não pode ser maior que "Terminar em". Favor digitar novamente!')
    com=int(input('Comerçar por: '))
    ter=int(input('Terminar em: '))
    print('='*120)
print('Vou montar a tabuada do {} começando em {} e terminando em {}'.format(tab,com,ter))
for x in range(com,ter+1):
    a=tab*x
    print('{} X {} = {}'.format(tab,x,a))
print('='*120)
os.system('pause')

