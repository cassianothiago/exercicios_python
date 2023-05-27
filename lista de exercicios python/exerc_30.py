import os
print('='*120)
print('.Loja quase dois.')
print('='*120)
print('TABELA DE PREÇOS')
a=50
b=1.99
for x in range(1,51):
    c=b*x
    print('{} - R$ {:.2f}'.format(x,c))

print('='*120)
print('.Panificadora pão de ontem.')
print('='*120)
d=float(input('Preço do pão?: '))
print('TABELA DE PREÇOS')
for w in range(1,51):
    e=d*w
    print('{} - R$ {:.2f}'.format(w,e))

print('='*120)
print('.Loja Tabajara.')
print('='*120)
print('.CAIXA REGISTRADORA.')
cont=0
soma=0
while True:
    cont=cont+1
    r=(input('qual é o produto ou digite zero para saber o valor da venda: '))
    if r=='0':
        break
    t=int(input('A quantidade comprada do produto: '))
    q=float(input('digite o valor unitário do produto: '))
    y=t*q
    soma=soma+y
    print('*'*80)
    print('{}- {} = quantidade({} unidades) X valor de uma unidade(R$ {}) = R$ {:.2f}'.format(cont,r,t,q,y))
    print('*'*80)
print('='*120)
print('Total da compra =  R$ {:.2f}'.format(soma))
k=float(input('Total do pag em dinheiro: '))
troco=k-soma
print('='*120)
print('Troco para devolver ao cliente {:.2f} R$'.format(troco))
print('='*120)
os.system('pause')
