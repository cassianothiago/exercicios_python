#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.

a=int(input('Quantos CDs tem na sua coleção: '))
soma=0
print('='*120)
for x in range(a):
    print('qual foi o valor do ',x+1,'º CD?')
    valor=int(input('Valor: '))
    soma=soma+valor
print('='*120)
print('soma dos CDs = ',soma)
media=soma/a
print('media gasta por cd = ',media)
