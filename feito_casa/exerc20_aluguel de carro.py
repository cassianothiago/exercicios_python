km=int(input('digite quantos km vc rodou: '))
dias=int(input('digite quantos dias vc ficou com o carro: '))
preço_dia=int(60*dias)
preço_km=float(0.15*km)
preco_final=float(preço_dia+preço_km)
print('='*120)
print('preço por kilometragem foi %.2f R$ e por dia foi %d R$ com o total de : %.2f R$'%(preço_km,preço_dia,preco_final))
print('='*120)
