#1.	Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
print('='*120)

nota=float(input('digite uma nota entre zero e dez: '))
while nota<0 or nota>10:
    print('valor inválido')
    nota=float(input('digite uma nota entre zero e dez: '))
print('nota =',nota)
print('='*120)
