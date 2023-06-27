import pandas as pd
#dataframe=pd.DataFrame()
'''print('-----')
venda={'data':['26/06/2023','27/06/2023'],'valor':[15,20],'produto':['feijão','arroz'],'qtde':[50,70]}
print(venda)
tabela_vendas=pd.DataFrame(venda)
print('-----')
print(tabela_vendas)
print('-----')'''
tabela_vendas=pd.read_excel('Vendas.xlsx')
print(tabela_vendas)


