#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

import os
turmas=int(input('digite quantidade de turmas: '))
soma=0
for i in range(turmas):
    
    print('cadastro da turma ',i+1)
    alunos=int(input('digite a quantidade de alunos da turma: '))
    while alunos>40:
        print('>40')
        alunos=int(input('digite a quantidade de alunos da turma: '))

    if alunos<40:
        soma=soma+alunos
        cont=cont+1

print(soma)
os.system('pause')

    
