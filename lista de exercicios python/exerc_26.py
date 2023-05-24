#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
print('='*120)
print('cadstro da idade dos alunos da turma')
print('='*120)
cont=0
soma=0
alunos=int(input('digite a quantidade de alunos matriculados'))
while cont<=alunos:
    cont=+1
    idade=int(input('Digite a idade do aluno: '))
    soma=soma+idade
    media=soma/alunos
print('A sala tem {} de alunos e a média de idade é {}'.format(alunos,media))
if media
