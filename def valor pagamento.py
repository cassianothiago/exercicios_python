
def valorpagamento(valor,dias):
    pagamento=valor+(valor*0.03+dias*0.001*valor)
    return pagamento


print('caixa')
dic={}
listaprest=[]
listaatraso=[]
listpag=[]
while True:
    prest=float(input('Digite o valor da prestação ou zero pra sair e imprimir: '))
    listaprest.append(prest)
    if prest==0:
        break
    atraso=int(input('Digite os dias de atraso ou zero se estiver em dia: '))
    listaatraso.append(atraso)
    if atraso>0:
        pag=valorpagamento(prest,atraso)
        listpag.append(pag)
    elif atraso==0:
        listpag.append(prest)
    dic={'prestação':listaprest,'atraso de ':listaatraso,'valor total':listpag}
print(dic)
