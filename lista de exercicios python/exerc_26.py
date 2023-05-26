#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

import os
print('='*120)
print('cadstro da idade dos alunos da turma')
print('='*120)
cont=0
soma=0
cont2=0
alunos=int(input('digite a quantidade de alunos matriculados: '))
while cont<alunos:
    cont=cont+1
    idade=int(input('Digite a idade do aluno: '))
    soma=soma+idade
    media=soma/alunos
    if idade>0 and idade<=25:
        cont2=cont2+1
print('quantidade de jovens é: ',cont2)
print('='*120)
print('A sala tem {} alunos e a média de idade é {}'.format(alunos,media))
print('='*120)
if media>0 and media<=25:
    print('A turma é jovem')
elif media>25 and media<=60:
    print('A turma é adulta')
else:
    print('A turma é idosa')
print('='*120)
os.system('pause')
