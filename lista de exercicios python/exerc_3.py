#3.	Faça um programa que leia e valide as seguintes informações:
#a.	Nome: maior que 3 caracteres;
#b.	Idade: entre 0 e 150;
#c.	Salário: maior que zero;
#d.	Sexo: 'f' ou 'm';
#e.	Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

print('='*120)
nome=input('digite um nome com mais de 3 caracteres: ')
a=len(nome)
while a<=3:
    print('favor digitar nome com mais de 3 caracteres. Digite novamente')
    nome=input('digite um nome: ')
    a=len(nome)

print('='*120)    
idade=int(input('digite uma idade entre 0 e 150 anos: '))
while idade<0 or idade>150:
    print('favor digitar uma idade entre 0 e 150 anos. Digite novamente!')
    idade=int(input('digite uma idade: '))

print('='*120)
salario=float(input('digite um salario maior que zero: '))
while salario<=0:
    print('favor digitar um salario maior que zero. Digite novamente!')
    salario=float(input('digite salario: '))

print('='*120)
sexo=(input('digite seu genero; M para masculino ou F para feminino: '))

#and 
while (sexo!='M') and (sexo!='F') and (sexo!='m') and (sexo!='f'):
    print('genero inválido. Favor digitar novamente!')
    sexo=input('digite M para masculino ou F para feminino: ')
sexo=sexo.capitalize()

if sexo!='M' or sexo!="F": # Se um dos dois for verdade ele entra
    print('genero masculino')
elif sexo=='F':
    print('genero feminino')
print('='*120)
print('.')
