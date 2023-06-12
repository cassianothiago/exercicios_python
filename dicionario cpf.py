
dicionario={}
while True:
    cpf=int(input('digite seu cpf ou zero para imprimir: '))
    if cpf==0:
        break
    nome=(input('digite o nome: '))
    idade=(input('digite sua idade: '))
    tel=(input('digite seu tel: '))
    
    dicionario[cpf]={'nome':nome,'idade':idade,'tel':tel}
print(dicionario)
   


