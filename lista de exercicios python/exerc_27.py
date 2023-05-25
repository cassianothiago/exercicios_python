#27.	Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

import os
print('='*120)
elet=int(input('Digite quantos eleitores: '))
cont=0
lista=[]
print('='*120)
while cont<elet:
    cont=cont+1
    print('eleitor ',cont)
    print('vote conferme a legenda')
    print('1-votar em fulano \n2-votar em ciclano \n3-votar em beltrano')
    voto=int(input('digite seu voto: '))
    print('='*120)
    lista.append(voto)
    os.system('cls')
cont_vot1=lista.count(1)
cont_vot2=lista.count(2)
cont_vot3=lista.count(3)
print('='*120)
print('total de votos: candidato fulano =  ',cont_vot1)
print('total de votos: candidato ciclano = ',cont_vot2)
print('total de votos: candidato beltrano = ',cont_vot3)
print('='*120)
if cont_vot1>cont_vot2 and cont_vot1>cont_vot3:
    print('O candidatos fulano venceu as eleiçoes!!!')
elif cont_vot2>cont_vot1 and cont_vot2>cont_vot3:
    print('O candidatos ciclano venceu as eleiçoes!!!')
elif cont_vot3>cont_vot1 and cont_vot3>cont_vot2:
    print('O candidatos beltrano venceu as eleiçoes!!!')
elif cont_vot1==cont_vot2 and cont_vot1>cont_vot3:
    print('candidatos fulano e ciclano estão empatados!!!')
elif cont_vot1==cont_vot3 and cont_vot1>cont_vot2:
    print('candidatos fulano e beltrano estão empatados!!!')
elif cont_vot2==cont_vot3 and cont_vot2>cont_vot1:
    print('canditados ciclano e beltrano estão empatados!!!')
else:
    print('todos os candidatos estão empatados!!!')
os.system('pause')
