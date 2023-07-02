import os
import pandas
import math

def valor():
    multa=float(input('Valor da multa: '))
    juros=float(input('Valor dos juros: '))
    total=conta+((conta*multa/100)+(conta*juros))
    return total
def troco(total):
    while dinheiro<total:
        dinheiro=float(input('valor em dinheiro: '))
        troco=dinheiro-total
        
        return troco

print('-----')
print('Bem vindo ao caixa')
saldo_inicial=float(input('Qual seu saldo inicial: '))
print('-----')
cont=0
cont2=0
list_cliente=[]
list_conta=[]
list_atraso=[]
list_valor=[]
list_troco_cliente=[]
while True:
    cont=cont+1
    cliente=input('Nome do {}º cliente ou zero para encerrar: '.format(cont))
    if cliente=='0':
        break
    list_cliente.append(cliente)
    while True:
        cont2=cont2+1
        conta=float(input('Valor da {}ª conta ou zero para encerrar: '.format(cont2)))
        if conta==0 or conta==0:
            break
        list_conta.append(conta)
        atraso=int(input('A {}ª conta está atrasada? quantos dias? digite zero se não estiver atrasada: '.format(cont2)))
        if atraso>0:
            pag=valor()
            list_valor.append(pag)
        else:
            list_valor.append(conta)
        list_atraso.append(atraso)
    pagamento=sum(list_valor)
    dinheiro=float('Digite o valor do dinheiro: ')
    
    while dinheiro<pagamento
        
    
    
print(list_cliente)
print(list_conta)
print(list_atraso)
print(list_valor)
print(list_troco_cliente)    