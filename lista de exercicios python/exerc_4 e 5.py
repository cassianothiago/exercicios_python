"""4.	Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
   5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

print('='*120)
a=80000
b=200000
txa=0.03
txb=0.015
ano=0

while a<b:
    a=a+(a*txa)
    b=b+(b*txb)
    ano=ano+1
print('em {} anos a populacao do país A supera a população do país B'.format(ano))
print('='*120)

a=float(input('Digite a população do primeiro país: '))
b=float(input('Digite a população do segundo país: '))
txa=float(input('Digite a taxa de crescimento do primeiro país: '))
txb=float(input('Digite a taxa de crescimento do segundo país: '))
ano=0
while a<b:
    a=a+(a*txa)
    b=b+(b*txb)
    ano=ano+1
print('='*120)
print('em {} anos a população do primeiro país será maior que a população do segundo país'.format(ano))
print('='*120)
print('em {} anos a população do primeiro país será de {:.0f} e sua taxa de crescimento anual é {}% e a população do segundo país será de {:.0f} e sua taxa de crescimento anual é {}%'.format(ano,a,(txa*100),b,(txb*100)))
print('='*120)
