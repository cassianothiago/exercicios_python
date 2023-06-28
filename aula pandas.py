import pandas as pd
#dataframe=pd.DataFrame()
#print(dataframe)
'''venda={'data':['26/06/2023','27/06/2023'],'valor':[15,20],'produto':['feijão','arroz'],'qtde':[50,70]}
print(venda)
tabela_vendas=pd.DataFrame(venda)
print(tabela_vendas)'''
tabela_vendas=pd.read_excel("Vendas.xlsx")
#print(tabela_vendas)
#print(tabela_vendas.head())
#print(tabela_vendas.shape)
#print(tabela_vendas.describe())
#produtos=tabela_vendas[['Produto','ID Loja']]
#print(produtos)
#print(tabela_vendas.loc[1:2])
#print(tabela_vendas.loc[tabela_vendas['ID Loja']=='Norte Shopping'])
#vendas_NorteShopping=tabela_vendas.loc[tabela_vendas['ID Loja']=='Norte Shopping']
#print(vendas_NorteShopping.head(1))
vendas_NorteShopping=tabela_vendas.loc[tabela_vendas['ID Loja']=='Norte Shopping',['Produto','Quantidade']]
print(vendas_NorteShopping)
print(tabela_vendas.loc[4,'Produto'])




