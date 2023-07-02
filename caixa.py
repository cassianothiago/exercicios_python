import os
import pandas as pd
import math

def valor(conta):
    multa=float(input('Valor da multa: '))
    juros=float(input('Valor dos juros: '))
    total=conta+((conta*multa/100)+(conta*juros))
    return total
def troco(pagamento,dinheiro):
    troco=dinheiro-pagamento
    print('Troco para devolver = {:.2f}'.format(troco))
    while True:
            nota=float(input('Digite o Valor da nota ou zero para encerrar: '))
            if nota==0:
                break
            saldo=troco-nota
            troco=saldo
            print('Troco para devolver = {:.2f}'.format(saldo))
            return saldo

print('-----')
print('Bem vindo ao caixa')
saldo_inicial=float(input('Qual seu saldo inicial: '))
print('-----')
cont=0
cont2=0
list_cliente=[]
list_atraso=[]
list_pagamento=[]
list_valor=[]
list_dinheiro=[]
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
            cont2=0
            break
        atraso=int(input('A {}ª conta está atrasada? quantos dias? digite zero se não estiver atrasada: '.format(cont2)))
        if atraso>0:
            pag=valor(conta)
            list_valor.append(pag)
            
        else:
            list_valor.append(conta)
        list_atraso.append(atraso)
        pagamento=sum(list_valor)
        list_pagamento.append(pagamento)
    print(pagamento)
    dinheiro=float(input('Digite o valor em dinheiro: '))
    list_dinheiro.append(dinheiro)
    resto=troco(pagamento,dinheiro)
    print(resto)
    continue
caixa={'Cliente':[list_cliente],'Contas':[list_pagamento],'Atraso':[list_atraso],'Dinheiro':[list_dinheiro]}
tabela_caixa=pd.DataFrame(caixa)
flog=input('Digite I para imprimir todo o flog ou o nome do cliente para imprimir apenas o dele: ')
if flog=='i' or flog=='I':
    print(tabela_caixa)
else:
    print(tabela_caixa.loc[tabela_caixa]=='flog')
      
        
           
        
    
    
