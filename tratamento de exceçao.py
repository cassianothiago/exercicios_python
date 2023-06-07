import os
print('='*120)

print('========cadastro aeroporto======')
print('')

lista_cc=[]
lista_cp=[]
lista_ct=[]
lista_ca=[]
while True:
    try:
        print('')
        a=(input('Digite \n(1) para cadastro de cliente\n(2) para cadastro de passagem\n(3) para cadastro de tripulação\n(4) cadastro de avião\n(5) relatorio\n(0) para sair\n:  '))
        print('')
    except ValueError:
        print('digito invalido')
    except:
        print('erro desconhecido')
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
                    lista_cc.append(nome)
                    lista_cc.append(sobrenome)
                    lista_cc.append(rg)
                    lista_cc.append(cpf)
                    lista_cc.append(endereço)
                    lista_cc.append(fone)
                    lista_cc.append(idade)
                    break

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
                    lista_cp.append(destino)
                    lista_cp.append(origem)
                    lista_cp.append(duracao)
                    lista_cp.append(valor)
                    lista_cp.append(desconto)
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
                    lista_ct.append(nomet)
                    lista_ct.append(cargo)
                    lista_ct.append(idadet)
                    lista_ct.append(admissao)
                    lista_ct.append(fonet)
                    break

    elif a=='4':
            while True:
                try:
                    print('')
                    print('CADASTRO DE AVIÃO')
                    print('')
                    modelo=(input('Modelo do avião: '))
                    ano=(input('Ano: '))
                    cor=(input('cor do avião: '))
                    horas=(input('Horas de voo: '))
                    capacitade=(input('Capacidade de passageiros: '))
                except ValueError:
                    print('digito inválido')
                    continue
                except:
                    print('erro desconhecido')
                    continue
                else:
                    lista_ca.append(modelo)
                    lista_ca.append(ano)
                    lista_ca.append(cor)
                    lista_ca.append(horas)
                    lista_ca.append(capacitade)
                    break

    elif a=='0':
            break

    elif a=='5':
                print(*lista_cc,sep='\n')
                print(*lista_cp,sep='\n')
                print(*lista_ct,sep='\n')
                print(*lista_ca,sep='\n')
    os.system('pause')
    os.system('cls')

