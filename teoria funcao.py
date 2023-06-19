'''def hello():
    print('olá')

hello()'''

'''def hello2(nome):
    print('olá',nome)




a = input('digite: ')
hello2('thiago')'''

'''def hello3(nome,idade):
    print('olá',nome,'\nsua idade é :',idade)

hello3('miguel',7)'''

'''def calcular_pag(quant_hora,valor_hora):
    horas=float(quant_hora)
    taxa=float(valor_hora)
    if horas <=40:
        salario=horas*taxa
    else:
        h_exced=horas-40
        salario=40*taxa+(h_exced*(1.5*taxa))
    print(salario)

calcular_pag(30,60)
calcular_pag(50,60)'''

def soma(x,y):
    result=x+y
    return result

a=int(input('digite o primeiro numero: '))
b=int(input('digite o segundo numero: '))
soma(a,b)
res=soma(a,b)
print('soma = ',res)

