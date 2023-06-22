
def valorpagamento(valor,dias):
    pagamento=valor+(valor*0.03+dias*0.001)
    return pagamento


print('caixa')
listprest=[]
listdias=[]
listpag=[]
prest=float(input('Digite o valor da prestação: '))
listprest.append(prest)
atraso=int(input('Digite os dias de atraso ou zero se estiver em dia: '))
if atraso>0:
    listdias.append(atraso)
    x=valorpagamento(prest,atraso)
    listpag.append(x)
print(listprest)
print(listdias)
print(listpag)

