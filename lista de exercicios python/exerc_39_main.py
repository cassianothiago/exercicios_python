from exerc_39 import*
print('calculo do novo salario de 1997 até 2023')
print('-----')
sal_ini=float(input('Digite o salario em 1996 = '))
porc_aumento=float(input('Digite a porcentagem de aumento salario em 1996 = '))
print('-----')
print('Aumento em 1997 = ',porc_aumento)
sal_97=sal_ini+(sal_ini*porc_aumento)
print('Sálario em 1997= {:.2f}'.format(sal_97))


salario_novo=Salario_97(sal_97,porc_aumento)


salario_novo.n_salario(sal_97,porc_aumento)
