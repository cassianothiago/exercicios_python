

listacliente=[]
listaprest=[]
listdias=[]
print('='*120)
print('-----')
inicial=float(input('Bem vindo ao caixa!!\n Qual seu saldo inicial:  '))

while True:
    cliente=input('digite o nome do cliente ou S para sair: ')
    if cliente=='s' or cliente=='S':
        break
    listacliente.append(cliente)
    prest=float(input('digite o valor da conta: '))
    dias=int(input('digite quantos dias está em atraso: '))
    listdias.append(dias)
    if dias>0:
        pagamento=prest+(prest*0.03+dias*0.001*prest)
        prest=pagamento
        listaprest.append(prest)
    elif dias==0:
        listaprest.append(prest)
    
for i in range(len(listacliente)):
        print('-----')
        print('cliente:',listacliente[i],'\nprestação:',listaprest[i],'\natraso:',listdias[i])
print('-----')
prestsoma=sum(listaprest)
print('total dos cliente: {:.2f}'.format(prestsoma))
while True:
     flog=input('imprimir o flog do cliente? digite seu nome! ou E para encerrar e ver saldo de caixa: ')
     if flog=='E' or flog=='e':
          saldofinal=inicial-sum(listaprest)
          print('Saldo em caixa = {:.2f}'.format(saldofinal))
          break
     else:
        a=listacliente.index(flog)
        print('-----')
        print('cliente:',listacliente[a],'\nprestação:',listaprest[a],'\natraso',listdias[a])
print('='*120)

             
    