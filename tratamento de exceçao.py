import os
print('='*120)

print('========cadastro aeroporto======')
print('')

lista_cc=[]
lista_cp=[]
lista_ct=[]
lista_ca=[]
while True:
    a=(input('Digite \n(1) para cadastro de cliente\n(2) para cadastro de passagem\n(3) para cadastro de tripulação\n(4) cadastro de avião\n(5) relatorio\n(0) para sair\n:  '))
    if a=='1':
        while True:
            try:
                print('')
                print('CADASTRO DE CLIENTE')
                print('')
                nome=(input('Nome do cliente: '))
                sobrenome=(input('Sobrenome do cliente: '))
                rg=int(input('Numero do RG: '))
                cpf=int(input('CPF: '))
                endereço=(input('Endereço: '))
                fone=int(input('Nº do telefone: '))
                idade=int(input('Idade: '))
            except ValueError:
                print('digito inválido')
                continue
            except:
                print('erro desconhecido')
                continue
            else:
                lista_cc.append(nome,sobrenome,rg,cpf,endereço,fone,idade)
                os.system('pause')
                os.system('cls')
                #break
        os.system('pause')
        os.system('cls')
    elif a=='2':
        while True:
            try:
                print('')
                print('CADASTRO DE PASSAGEM')
                print('')
                destino=(input('Destino do voo: '))
                origem=(input('Origem do voo: '))
                duracao=int(input('Duração do voo em horas: '))
                valor=float(input('Valor da passagem: '))
                desconto=valor-(valor*5/100)
                print('valor com desconto ',desconto)
            except ValueError:
                print('digito inválido')
                continue
            except:
                print('erro desconhecido')
                continue
            else:
                lista_cp.append(destino,origem,duracao,valor,desconto)
                break
    elif a=='3':
        while True:
            try:
                print('')
                print('CADASTRO DE TRIPULAÇÃO')
                print('')
                nomet=(input('Digite o nome: '))
                cargo=(input('Descrição do cargo: '))
                idadet=(input('Digite a Idade: '))
                admissao=(input('Data de admissão: '))
                fonet=int(input('Telefone: '))
            except ValueError:
                print('digito inválido')
                continue
            except:
                print('erro desconhecido')
                continue
            else:
                lista_ct.append(nomet,cargo,idadet,admissao,fonet)

    elif a=='4':
        while True:
            try:
                print('')
                print('CADASTRO DE AVIÃO')
                print('')
                modelo=(input('Modelo do avião: '))
                ano=int(input('Ano: '))
                cor=(input('cor do avião: '))
                horas=int(input('Horas de voo: '))
                capacitade=int('Capacidade de passageiros:')
            except ValueError:
                print('digito inválido')
                continue
            except:
                print('erro desconhecido')
                continue
            else:
                lista_ca(modelo,ano,cor,horas,capacitade)
                break
    elif a=='0':
        break
    elif a=='5':
            print(lista_cc)
            print(lista_cp)
            print(lista_ct)
            print(lista_ca)
os.system('pause')
os.system('cls')

