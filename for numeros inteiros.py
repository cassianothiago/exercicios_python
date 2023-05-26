print('='*120)
print('intervalo entre os numeros')
a=int(input('digite o 1º numero: '))
b=int(input('digite o 2º numero: '))
soma=0
print('os intervalos entre {} e {} são: '.format(a,b))
for x in range(a,b):
    print(x)
    soma=soma+x
print('e a soma dos intervalos = {}'.format(soma))
print('='*120)
