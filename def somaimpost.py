import os
def somaimposto():
    custo=float(input('digite o valor do custo do produto: '))
    impost=float(input('digite o valor do imposto em %: '))
    somaimposto=custo+(custo*(impost/100))
    return somaimposto



print('calculo de preço com imposto')
preco=somaimposto()
print(preco)

def somaimposto2(custo,imposto):
    somaimposto=custo+(custo*(imposto/100))
    return somaimposto

print('calculo de preco com imposto')
custo2=float(input('digite o valor do custo do produto: '))
impost2=float(input('digite o valor do imposto em %: '))
preco2=somaimposto2(custo2,impost2)
print(preco2)

os.system('pause')