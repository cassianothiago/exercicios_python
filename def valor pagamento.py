

def pagamento(prest,dias):
    
    pagamento=prest+(prest*0.03+0.01*dias)
    return pagamento





listaprest=[]
listadias=[]

print('pagamento caixa')
while True:
    prest1=float(input('digite o valor da prestação: '))
    listaprest.append(prest1)
    dias1=int(input('digite quantos dias está atrasado: '))
    if dias1!=0:
        pagamento(prest1,dias1)
        listadias.append()
    a=input('tecle enter para mais contas ou S para sair:')
    if a=='S' or a=='s':
        break    
    continue
print(listaprest)
print(listadias)

    