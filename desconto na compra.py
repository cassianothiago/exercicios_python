def valorpagamneto():
    listvalor=[]
    listdias=[]
    listapag=[]
    valor=float(input('Digite o valor da prestação: '))
    listapag.append(valor)
    dias=int(input('Digite quantos dias está atrasado, se estiver na data digite zero: '))
    listdias.append(dias)
    if dias>0:
        pagamneto=valor+(valor*0.03+dias*0.001)
        listvalor.append(pagamneto)
    print(listvalor)
    print(listdias)
    print(listapag)
    




print('caixa de pagamento')
while True:
    prest=float(input('Digite o valor da prestação: '))
    atraso=int(input('Digite quantos dias está atrasado, se estiver na data digite zero: '))
    valorpagamneto()
    

    



