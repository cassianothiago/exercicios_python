14.	#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

print('='*120)
base=int(input('digite um numero para base da potenciação: '))
exp=int(input('digite o numero para ser o expoente da potenciação: '))
pot=base**exp
print('O resultado de {} elevado a {} é {}'.format(base,exp,pot))
print('='*120)
