'''5.	Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
d.	Código da cidade;
e.	Número de veículos de passeio (em 1999);
f.	Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
g.	Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
h.	Qual a média de veículos nas cinco cidades juntas;
i.	Qual a média de acidentes de trânsito nas cidades com menos de 2.000'''

list_cod=[1,2,3,4,5]
list_cidade=['Campo Grande','São Paulo','Cuiaba','Curitiba','Recife']
list_veiculos=[1132,5743,1589,3526,4621]
list_vitimas=[120,250,130,125,232]
list_menmor2000=[]

maior_acident=max(list_vitimas)
menor_acident=min(list_vitimas)
cidade_maior_acident=list_cidade.index(maior_acident)
cidade_menor_acident=list_cidade.index(menor_acident)
media_veiculos=sum(list_veiculos)/5
a=list_veiculos<200
print(a)

    
