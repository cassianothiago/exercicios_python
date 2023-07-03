import pandas as pd
import os


print('Bem vindo ao Caixa')
print('-----')
inicial=float(input('Digite o valor de abertura do caixa: '))
cont=0
cont2=0
list_cliente=[].pop(-1)
list_conta=[].pop(-1)
list_atraso=[].pop(-1)
list_pagamento=[].pop(-1)

while True:
    list_valor=[]
    cont=cont+1
    cliente=(input('Nome do {}ª cliente ou zero para encerrar: '.format(cont)))
    list_cliente.append(cliente)
    if cliente=='0':
        break
    while True:
        cont2=cont2+1
        conta=float(input('Valor da {}ª conta do cliente {} ou zero para encerrar: '.format(cont2,cliente)))
        list_conta.append(conta)
        if conta==0:
            cont2=0
            break
        atraso=int(input('A {}ª conta do cliente {} esta atrasada? quantos dias?(se nenhum digite zero): '.format(cont2,cliente)))
        list_atraso.append(atraso)
        if atraso>0:
            multa=float(input('Valor da multa sem a porcentagem: '))
            juros=float(input('Valor do juros sem a porcentagem: '))
            valor=conta+(conta*(multa/100))+(conta*atraso*(juros/100))
            list_valor.append(valor)
        else:
            valor=conta
            list_valor.append(valor)
        pagamento=sum(list_valor)
        list_pagamento.append(pagamento)
        print('Valor para pagamento do cliente {} = {:.2f}'.format(cliente,pagamento))
    dinheiro=float(input('Valor entregue pelo cliente: '))
    troco=dinheiro-pagamento
    print('Troco para retornar ao cliente {} = {}'.format(cliente,troco))
    while True: 
        nota=float(input('Valor total das notas ou zero para encerar: '))
        if nota==0:
            break
        retorno_nota=troco-nota
        if retorno_nota>0:
            print('falta retornar: {:.2f} '.format(retorno_nota))
            troco=retorno_nota
        elif retorno_nota<0:
            print('Valor retornado a maior: ',retorno_nota)
while True: 
    flog=(input('Imprimir todo o flog digite I ou específico digite o nome do cliente ou zero para encerrar: '))
    if flog=='0':
        break
    if flog=='i' or flog=='I':
        imprimir_flog={'Cliente':[list_cliente],'Conta':[list_conta],'Atraso':[list_atraso],'Valor':[list_pagamento]}
        tabela_flog=pd.DataFrame(imprimir_flog)
        print(tabela_flog)
        