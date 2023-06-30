'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes'''

import pandas as pd

listcliente=[]
listaltura=[]
listpeso=[]
listnome=[]
listsexo=[]
cont=0
print('-----')
while True:
    cont=cont+1
    cliente=int(input('Digite o código do cliente: '))
    nome=input('Nome do cliente: ')
    listnome.append(nome)
    sexo=input('Sexo do cliente: ')
    listsexo.append(sexo)
    listcliente.append(cliente)
    altura=float(input('Digite sua altura: '))
    listaltura.append(altura)
    peso=int(input('Digite seu peso: '))
    listpeso.append(peso)
    print('-----')
    a=input('Cadastrar proximo cliente tecle enter!. Ou zero para encerrar: ')
    print('-----')
    if a=='0':
        break
    else: 
        continue
alto=max(listaltura)
baixo=min(listaltura)   
gordo=max(listpeso)
magro=min(listpeso)
sum_altura=sum(listaltura)
sum_peso=sum(listpeso)
me_altura=sum_altura/cont
me_peso=float(sum_peso/cont)
print('-----')
print('Altura maxima = {:.2f}'.format(alto))
print('Altura minima= {:.2f}'.format(baixo))
print('Maior Peso = ',gordo)
print('Menor Peso = ',magro)
print('Média altura = {:.2f}'.format(me_altura))
print('Média Peso = {:.2f}'.format(me_peso))
print('-----')
arquivo={'Cód.cliente':listcliente,'Nome':listnome,'Altura':listaltura,'Peso':listpeso}
tabela=pd.DataFrame(arquivo)
print(tabela)
while True: 
    
    consulta=int(input('consultar aluno? Digite seu código ou zero(0) para encerrar:  '))
    if consulta==0:
        break
    else:
        print('-----')
        print(tabela.loc[tabela['Cód.cliente']==consulta])
