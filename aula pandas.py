import pandas as pd
#dataframe=pd.DataFrame()
'''print('-----')
venda={'data':['26/06/2023','27/06/2023'],'valor':[15,20],'produto':['feijão','arroz'],'qtde':[50,70]}
print(venda)
tabela_vendas=pd.DataFrame(venda)
print('-----')
print(tabela_vendas)
print('-----')'''
tabela_vendas=pd.read_excel("Vendas.xlsx")
#print(tabela_vendas)
#print(tabela_vendas.head(10))
#print(tabela_vendas.shape)
#print(tabela_vendas.describe())
#produtos=tabela_vendas[['Produto','ID Loja']]
#print(produtos.head())
#print(tabela_vendas.loc[1:5])
print(tabela_vendas.loc[tabela_vendas['ID Loja']=='Norte Shopping'])
x=tabela_vendas.loc[tabela_vendas['ID Loja']=='Norte Shopping']
print(x.head())


