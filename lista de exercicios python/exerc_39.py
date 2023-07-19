''''3.	Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a.	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário'''


salario_inicial_95=1000
aumento_96=0.000015
aumento=salario_inicial_95+(salario_inicial_95*0.015)
print(aumento_96)
print(aumento)
print('-----')
for i in range(26):
    print(i+1)
    aumento_96=aumento_96*2
    novo_aumento=aumento+(aumento*aumento_96)
    aumento=novo_aumento
    print('-----')
    print(aumento_96)
    print('salario = {:.2f}'.format(novo_aumento))
    print('------')

