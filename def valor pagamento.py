
def valorpagamento(valor,dias):
    pagamento=valor+(valor*0.03+dias*0.001*valor)
    return pagamento

def troco(dinheiro,total):
    troco=dinheiro-total
    return troco


print('='*120)
print('caixa')
print('-----')
dic={}
listaprest=[]
listaatraso=[]
listpag=[]

try:
    while True:
        prest=float(input('Digite o valor da prestação ou zero pra sair e imprimir: '))
        if prest==0:
            break
        listaprest.append(prest)
        atraso=int(input('Digite os dias de atraso ou zero se estiver em dia: '))
        listaatraso.append(atraso)
        if atraso>0:
            pag=valorpagamento(prest,atraso)
            listpag.append(pag)
        elif atraso==0:
            listpag.append(prest)
        dic={'prestação':listaprest,'atraso de ':listaatraso,'valor total':listpag}
    print('='*120)
    print(dic)


    total1=sum(listpag)
    print('total a pagar= {:.2f}'.format(total1))
    dinheiro1=float(input('Digite o valor em dinheiro: '))
    while dinheiro1<total1:
        print('valor inferior ao total de pagamento digite novamente')
        dinheiro1=float(input('Digite o valor em dinheiro: '))
    troco1=troco(dinheiro1,total1)
    print('-----')
    print('Troco a devolver= {:.2f}'.format(troco1))
    while True:
        nota=float(input('Digite o valor da nota ou zero para sair = '))
        if nota==0:
            break
        saldo=troco1-nota
        troco1=saldo
        print('saldo parcial: {:.2f}'.format(troco1))
    print('-----')
    print('Saldo em caixa dessa operação = {:.2f}'.format(troco1))
    print('='*120)
except ValueError:
    print('valor digitado invalido')
except ZeroDivisionError:
    print('operação invalida div 0')
except:
    print('erro dieconhecido')
