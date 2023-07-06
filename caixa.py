import pandas as pd
import os

cont=0
cont2=0
list_cliente=[]
list_conta=[]
list_atraso=[]
list_valor=[]  

print('Bem vindo ao Caixa')
print('-----')
while True:
    try:
        inicial=float(input('Digite o valor de abertura do caixa: '))
        inicial=True
    except ValueError:
        print('saldo não reconhecido')
        inicial=False
    except:
        print('erro')
        inicial=-False
    
    if inicial is True:
        while True:
            try:
                cont=cont+1
                cliente=(input('Nome do {}ª cliente ou zero para encerrar: '.format(cont)))
                list_cliente.append(cliente)
            except ValueError:
                print('Inválido digite novamente')
            except:
                print('erro')
            if  cliente=='0':
                list_cliente.pop(-1)
                break
            while True:
                try:
                    cont2=cont2+1
                    conta=float(input('Valor da {}ª conta do cliente {} ou zero para encerrar: '.format(cont2,cliente)))
                    conta=True
                except ValueError:
                    print('valor da conta invalido digite novamente')
                    cont2=0
                    conta=False
                except:
                    print('erro')
                    cont2=0
                    conta=False
                if conta is True:
                    list_conta.append(conta)
                    if conta==0:
                        cont2=0
                        list_conta.pop(-1)
                        break
                    while True:
                        try:
                            atraso=int(input('A {}ª conta do cliente {} esta atrasada? quantos dias?(se nenhum digite zero): '.format(cont2,cliente)))
                        except ValueError:
                            print('Digite apenas quantos dias está atrasado')
                        except:
                            print('erro')
                        while atraso<0:
                            print('Atraso não pode ser negativo')
                            atraso=int(input('A {}ª conta do cliente {} esta atrasada? quantos dias?(se nenhum digite zero): '.format(cont2,cliente)))
                        if atraso==0:
                                list_atraso.append(atraso)
                                continue
                        elif atraso>0:
                                multa=float(input('Valor da multa sem a porcentagem: '))
                                juros=float(input('Valor do juros sem a porcentagem: '))
                                valor=conta+(conta*(multa/100))+(conta*atraso*(juros/100))
                                list_valor.append(valor)
                                continue
                        else:
                                list_valor.append(conta)
                                pagamento=sum(list_valor)
                                print('Valor para pagamento do cliente {} = {:.2f}'.format(cliente,pagamento))
                                dinheiro=float(input('Valor entregue pelo cliente: '))
                                troco=dinheiro-pagamento
                                print('Troco para retornar ao cliente {} = {}'.format(cliente,troco))
                while True: 
                        nota=float(input('Valor total das notas ou zero para encerar: '))
                        if nota==0:
                            break
                        retorno_nota=troco-nota
                        if retorno_nota>0:
                            print('falta retornar: {:.2f} '.format(retorno_nota))
                            troco=retorno_nota
                        elif retorno_nota<0:
                            print('Valor retornado a maior: ',retorno_nota)
                while True:
                    flog=(input('Imprimir todo o flog digite I ou específico digite o nome do cliente ou zero para encerrar: '))
                    if flog=='0':
                        break
                    if flog=='i' or flog=='I':
                        
                        imprimir_flog={'Cliente':[list_cliente],'Conta':[list_conta],'Atraso':[list_atraso],'Valor':[list_valor]}
                        tabela_flog=pd.DataFrame(imprimir_flog)
                        print(tabela_flog)
                    else:
                        find=list_cliente.index(flog)  
                        print(list_cliente[find],list_conta[find],list_atraso[find],list_valor[find])
                    