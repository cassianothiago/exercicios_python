#desenvolva um algoritmo que receba e armazene em uma lista , e posteriormente imprima os seguintes dados:
#nome, sobrenome, endereço, bairro, cidade, estado, pais, tel, cpf, peso, altura, idade, numero cartão, email, cep, nota1, nota2, nota3, nota4, media, serie, classe, sexo,
#cor e matricula(automática cont)
import os
cont=0
lista_matricula=[]
lista_nome=[]
lista_sobrenome=[]
lista_rua=[]
lista_bairro=[]
lista_cidade=[]
lista_estado=[]
lista_CEP=[]
lista_pais=[]
lista_tel=[]
lista_CPF=[]
lista_peso=[]
lista_altura=[]
lista_idade=[]
lista_cart=[]
lista_email=[]
lista_not1=[]
lista_not2=[]
lista_not3=[]
lista_not4=[]
lista_media=[]
lista_serie=[]
lista_classe=[]
lista_sexo=[]
lista_cor=[]

print('cadastro de aluno')
while True:
    op=input("digite 1 para cadastro 2 para consulta 0 sair: ")
    if op=='0':           
        break

    if op=='1':           
        cont=cont+1
        matricula=cont
        nome=input('digite seu nome: ')
        sobrenome=input('digite seu sobrenome: ')
        rua=input('digite nome da rua: ')
        bairro=input('digite seu bairro: ')
        cidade=input('digite sua cidade: ')
        estado=input('digite seu estado: ')
        cep=int(input('digite seu CEP: '))
        pais=input('digite seu país: ')
        tel=int(input('digite seu telefone: '))
        cpf=int(input('digite seu cpf: '))
        peso=int(input('digite seu peso: '))
        altura=float(input('digite sua altura: '))
        idade=int(input('digite sua idade: '))
        cart=int(input('digite numero do cartão: '))
        email=input('digite seu email: ')
        not1=float(input('digite sua 1ª nota: '))
        not2=float(input('digite sua 2ª nota: '))
        not3=float(input('digite sua 3ª nota: '))
        not4=float(input('digite sua 4ª nota: '))
        media=(not1+not2+not3+not4)/4
        serie=int(input('digite sua série: '))
        classe=(input('digite sua classe: '))
        sexo=(input('digite m para masculino e f para feminino: '))
        if sexo=='M' or 'm':
            sexo=='Masculino'
        else:
            sexo=='Feminino'
        cor=(input('digite sua cor: '))
        lista_nome.append(nome)
        lista_sobrenome.append(sobrenome)
        lista_rua.append(rua)
        lista_bairro.append(bairro)
        lista_cidade.append(cidade)
        lista_estado.append(estado)
        lista_CEP.append(cep)
        lista_pais.append(pais)
        lista_tel.append(tel)
        lista_CPF.append(cpf)
        lista_peso.append(peso)
        lista_altura.append(altura)
        lista_idade.append(idade)
        lista_cart.append(cart)
        lista_email.append(email)
        lista_not1.append(not1)
        lista_not2.append(not2)
        lista_not3.append(not3)
        lista_not4.append(not4)
        lista_media.append(media)
        lista_serie.append(serie)
        lista_classe.append(classe)
        lista_sexo.append(sexo)
        lista_cor.append(cor)
        lista_matricula.append(matricula)
    if op=='2':     
        mat=int(input("Digite a matrícula: "))
        
        print(lista_matricula[mat-1],lista_nome[mat-1],lista_sobrenome[mat-1],lista_rua[mat-1],lista_bairro[mat-1],lista_cidade[mat-1],lista_estado[mat-1],lista_CEP[mat-1],lista_pais[mat-1],lista_tel[mat-1],lista_CPF[mat-1],lista_peso[mat-1],lista_altura[mat-1],lista_idade[mat-1],lista_cart[mat-1],lista_email[mat-1],lista_not1[mat-1],lista_not2[mat-1],lista_not3[mat-1],lista_not4[mat-1],lista_media[mat-1],lista_classe[mat-1],lista_serie[mat-1],lista_cor[mat-1])
os.system('pause')
