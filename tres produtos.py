print('='*120)

a=float(input('digite o valor do primeiro produto: '))
b=float(input('digite o valor do segundo produto: '))
c=float(input('digite o valor do terceiro produto: '))
nome_a=(input('digite o nome do primeiro produto: '))
nome_b=(input('digite o nome do segundo produto: '))
nome_c=(input('digite o nome do terceiro produto: '))

print('='*120)
if a<b and a<c:
    print('compre o produto {} que tem o valor de {}'.format(nome_a,a))
elif b<a and b<c:
    print('compre o produto {} que tem o valor de {}'.format(nome_b,b))
elif c<a and c<b:
    print('compre o produto {} que tem o valor de {}'.format(nome_c,c))
else:
    print('valores iguais')
print('='*120)
elif a==b:
    if c>a:
        print('primeiro e segundo produto tem o mesmo preco e estao mais baratos que o terceiro')
