

listacliente=[]
listaprest=[]
listdias=[]
cont=0
while True:
    cliente=input('digite o nome do cliente ou S para sair: ')
    if cliente=='s' or cliente=='S':
        break
    listacliente.append(cliente)
    prest=float(input('digite o valor da conta: '))
    listaprest.append(prest)
    dias=int(input('digite quantos dias está em atraso: '))
    listdias.append(dias)
for i in range(len(listacliente)):
    print('cliente:',listacliente[i],',prestação:',listaprest[i],'atraso:',listdias[i])
    
    