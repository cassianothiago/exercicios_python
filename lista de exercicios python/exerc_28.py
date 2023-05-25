#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

import os
turmas=int(input('digite quantidade de turmas: '))
cont=0
lista=[]
while cont<turmas:
    cont=cont+1
    print('cadastro da turma ',cont)
    alunos=int(input('digite a quantidade de alunos da turma: '))
    if alunos>40:
        print('numero de alunos por turma não pode ser maior que 40')
    continue

    
