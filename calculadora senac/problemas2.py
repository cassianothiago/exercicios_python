def tabuada():
    print("-----------------------------------")#Apresentação
    print("             Bem Vindo")
    print("                 a")
    print("              Tabuaba")
    print("-----------------------------------")
    num1 = int(input("Digite o número para fazer a tabuada: "))#Recebe um número e armazena
    mult = int(input("Informe até que número será multiplicado: "))#Recebe a quantidade de vezes que se deve multiplicar o número
    cont=0#Contador
    while mult>=cont:#Enquanto Estiver dentro do limite de quantidade de vezes para se multiplicar, ele irá continuar multiplicando
        result = num1*cont#Cálculo para a multiplicação
        print("%d x %d = %d"%(num1, cont, result)) #Escreve a conta
        cont=cont+1#aumenta em 1 o fator multiplicador
    print("------------------------------------")
    print("        Obrigado por usar")
    print("                a")
    print("             Tabuada")
    print("------------------------------------")

def feature30():   
    num=int(input("Digite um número: ")) # Pedir número que o usuário quer que reduza
    while num > 0:    # Função pede que enquanto maior que zero continue reduzindo
        num = (num-1) # Função para reduzir de um em um
        print(num) # O print nessa identação irá mostrar os números reduzindo um a um

def feature31(): # Faça um programa que leia um número do usuário e imprima todos os números de 0 até o número digitado.   
    num = int(input("Digite um número: ")) # Pedir número que o usuário quer que reduza até zero
    num = num +1 # Adiciono 1 para que o programa inicie com o número digitado
    while num > 0:    # Função pede que enquanto maior que zero continue reduzindo
        num = (num -1) # Função para reduzir de um em um
        print(num) # O print nessa identação irá mostrar os números reduzindo um a um
                
def feature32():
    import os
    print('Bem vindo a tabuada')
    a=int(input('digite o numero para afetuar a tabuada: '))
    cont=0
    while cont<10:
        cont=cont+1
        tab=a*cont
        print(a,'x',cont,'= ',tab)
    os.system('pause')

def feature33():
    print("----------Bem vindo a media por lista----------") 
    n1 = float(input("Digite o primeiro numero: ")) # Pede o primeiro numero para calculo
    n2 = float(input("Digite o segundo numero:  ")) # Pede o segundo numero para calculo
    n3 = float(input("Digite o terceiro numero: ")) # Pede o terceiro numero para calculo
    lista = [n1,n2,n3]                              #Lista dos numeros digitados
    final = sum(lista)/len(lista)                   #Calculo da média da lista
    print("A média da lista dos 3 elementos digitados é: ",final) #print do resultado
    print("----------Muito Obrigado----------")   
def feature34():
        print(print("----------------------Seja bem vindo aos Verificador de números pares!----------------------"))
        print("                                 Vamos Começar!")
        num=int(input("Digite até qual número você quer verificar se é Par: "))
        cont=2 #contador para que imprima os números pares
        while cont<=num: 
            if num%2==0: #se o número tiver resto 0 ele entre nessa condição de ser um número PAR 
                print(num)
            num-=1 
        print("Esses são os números pares!\n")
        print("----------------------OBRIGADO POR UTILIZAR O NOSSO VERIFICADOR!----------------------")
def feature35():
        print("---------------------------------------------")
        print("                Bem-Vindo                      ")
        print("---------------------------------------------")
        a=-1
        while a<=50:#Serve para aparecer só os numeros impares
         a=a+2
         print(a)#Imprimir todos os numeros impares
        print("---------------------------------------------")
        print("             Obrigado por usar                 ")
        print("---------------------------------------------")
def feature36():
    print("="*25, "Bem vindo a SENHA", "=" * 25)
    
    while True: #Laço de repetição
        senha = input("Digite uma senha para efetuar login: ")
        senha = senha.upper() #Deixar a senha em maiusculo para evitar erros
        if senha == "MAURICIO": #Caso seja verdadeiro
            print ("\nBem vindo, Sr. Mauricio\n")
            print ("="*25,"Obrigado por Usar a SENHA :)", "="*25)
            break
        else:
            print ("\nSenha incorreta! Tente novamente...\n")
            continue #Voltar no inicio caso a senha estiver errada!
        
def feature37():
    while True:
        op=int(input("\nAcerte o número sorteado entre 1 a 100 e ganhe um prêmio!\nDigite: "))
        if op==42:
            print("\nVocê Adivinhou o número, parabéns!!! Colete seu prêmio imediatamente!!!\n")
            break
        else:
            print("\nNúmero errado, tente novamente!\n")        
def feature38():
    print("======================================")
    print("|           SEJA BEM VINDO           |")
    print("|                                    |")
    print("======================================")
    soma = 0

    for c in range(1, 101):
        soma += c
    print(soma)# o codigo soma os numeros de 1 a 100 e soma , dando o valor final 
    print("Obrigado ! TENHA UM OTIMO DIA")
def feature39():
    print("------BEM VINDO! NÚMERO SECRETO. MAIOR OU MENOR.-------")
    secret=100 #Número secreto.
    num=int(input("Digite um número que você ache que seja o número secreto!: ")) #Usuário digita o número secreto.
    if num>secret: #Caso o número digitado sera maior.
        print("O número que você digitou é maior que o número secreto.")
    elif num<secret: #Caso seja menor.
        print("O número que você digitou é menor que o número secreto.")
    elif num==secret: #Caso o usuário acerte o número secreto.
        print("Parabéns! Você acertou!")
def feature40():
    a = 101
    print("Esses são os números de 100 a 1: ")
    while True:
        if a!=1:
            a = a - 1
            print(a)

def feature41():
    #o programa vai solicite ao usuário uma sequência de números e imprima o maior e o menor número digitados.
    nu=[]
    import os
    print('================================================================================')
    print('=                                  Bem Vindo                                   =') 
    print('================================================================================')    
    while True:
        op=input(' 1 - digite 1 para digitar um numero\n 2 - digite 2 para saber qual é o maior numero, e o menor numero\n Digite aqui: ')
        if op=='1':
            num=int(input('Digite qualquer numero: '))
            nu.append(num)
            os.system('cls')
        elif op=='2':
            print('O maior numero digitado foi: ',max(nu))
            print('O menor numero digitado foi: ',min(nu))
            break
    print('================================================================================')
    print('=                              Obrigado Volte Sempre                           =') 
    print('================================================================================')
#usei o os.system('cls') para limpar o terminal 
#usei o programa de list para salvar o numero digitado pelo usuario

def feature42():
    result=0
    while True:
        print("-------BEM VINDO!!!! LEITOR DE NUMEROS E SOMADOR!!-------")
        num=int(input("Digite um número: "))
        if num>=0:
            result=num+result
            continue
        elif num<0:
            result=result-num
            break
    print("O resultado da soma dos números digitados é {:d}".format(result))

def feature43():
    print ("="*100)
    print ("!                      B O A S - V I N D A S   A O   F A  T O R I A L                              !") 
    print ("="*100)
    print ("\n")

    n = int(input("Digite seu número para fatorar: "))
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i


    print ("A resposta do número fatorial %d! é %r"%(n,resultado))
    
    print ("\n")
    print ("="*100)
    print ("!                             O B R I G A D O   P O R   U S A R                                    !")
    print ("="*100)
def feature44(): # Crie um programa que leia números do usuário e conte quantos números pares e quantos números ímpares foram digitados.
    contpar=0
    contimpar=0
    print("\n           Bem vindo\nQuando desejar sair digite zero") # Boas vindas, informando que para sair do programa é só digitar o zero
    while True:        
        num = int(input("\nDigite um número: "))
        if num == 0:
            break
        elif (num%2 == 0): # Cálculo para condição de número par
            contpar = contpar +1    # Contador dos números pares   
        else: # Cálculo para condição de número impar
            contimpar = contimpar +1 # Contador dos números impares   
    print(contpar)   # Nesta identação irá imprimir a quantidade de números pares digitados
    print(contimpar) # Nesta identação irá imprimir a quantidade de números impares digitados
def feature45():
    print("-----------------------------------")#Apresentação
    print("             Bem Vindo")
    print("                 a")
    print("        Fórmula de Fibonacci")
    print("-----------------------------------")
    a=int(input("Digite um número onde irá parar: "))#Recebe o número
    ultimo=0
    penultimo=1
    termo=0
    while a>=termo:#Enquanto a variável "a" for maior que a variável"termo" irá rodar o programa
       print(termo)
       termo = ultimo + penultimo#Cálculo de Fibonacci
       penultimo = ultimo#Coloca a variável "ultimo" na adição 
       ultimo = termo#Coloca a variável "última" como resultado

    print("-----------------------------------")#Finalização
    print("          Obrigado por usar")
    print("                 a")
    print("        Fórmula de Fibonacci")
    print("-----------------------------------")

def feature46():
    num=0
    print("======SEJA BEM VINDO======") #essa funçao da boas vindas
    while True:
        num=num+3 #essa funçao vai ler os numeros
        print(num,"\n")
        if num==99:
            break
def feature47():
    import os
    secret_word = "fabrica108"
    print("===============================================\nBem Vindo!\nO programa a seguir é basicamente um desafio!\ntente adivinhar a palavra secreta, vamos começar?\n===============================================")
    word = input("Digite uma palavra ")
    while word != secret_word : # condição que mantem o loop 
        print("Errado!, tente novamente ")
        word = input("Digite uma palavra ")
        os.system("cls") # função para dar uma limpada no console
        if word == secret_word :
            print("Parabéns!_vc é exepcional_\ncomo recompensa se libertou do looping, fim...")
    print("================================================\nObrigado e até a próxima partida\n================================================")

    



def feature48():
    
    print("*",40*"-","*")
    print("|",40*" ","|")
    print(("|"+13*" "+"Seja bem vindo!!"+13*" "+"|")) # quadro mostrando 'seja bem vindo'
    print("|",40*" ","|")
    print("*",40*"-","*")
    print()
    cont = 0        # contador esta recebendo 0 para iniciar a contagem e para funcionar
    print("Digite um numero a soma dos numeros digitados sera somado\n"
    "ate chegar a mais de 100, quando chegar mais de 100 sera encerrado.\n")        # explicação do que vai acontecer para o usuario
    while True:             # laço de repetição, ficar em um loop
        num = float(input("Digite um numero: ")) #o usuario ira escrver um numero aqui
        cont = cont + num # contador para somar 
        print("Numero digitado %.0f e a soma é %.0f"%(num,cont))    # printando o resultado e o numero escrito pelo usuario
        if cont > 100:          #if usado para quando o cont for maior que 100 agradeçer e para o programa
            print("\nObrigado pela preferencia...\nVolte sempre.")      # sendo simpatico, e para voltar sempre
            break           # para parar po programa

def feature49(): #atividade pra mostrar os números primos entre 1 e 100
    list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #coloquei todos os números primos em uma lista
    while True:
        print("Esses são os números primos entre 1 e 100: ")
        print(list) #imprimi a lista
        break #pedi pra parar para não ficar imprimindo pra sempre

def feature50():
    
    print('       --- Bem vindo a Média ---')
    print('-'*40)
    nt1=float(input("> Infome seu primeiro número:"))
    nt2=float(input("> Infome seu segundo número:"))
    nt3=float(input("> Infome seu terceiro número:"))
    nt4=float(input("> Infome seu quarto número:"))
    if nt1 <0:
            media=(nt2+nt3+nt4) / 3
            print('> Sua média foi %.1f'%media)
    elif nt2 <0:
            media=(nt1+nt3+nt4) / 3
            print('> Sua média foi %.1f'%media)
    elif nt3 <0:
            media=(nt1+nt2+nt4) / 3
            print('> Sua média foi %.1f'%media)
    elif nt4 <0:
            media=(nt1+nt2+nt4) / 3
            print('> Sua média foi %.1f'%media)
    else:
        media = (nt1+nt2+nt3+nt4) / 4
        print('> Sua média foi %.1f'%media)
        print('-'*40)
        print('   --- Obrigado por usar Conosco! ---')

def feature51():
    num=int(input("Digite um número: ")) #Lê o número.
    while num>0: #Enquanto for maior que zero.
        test1=num%2
        test2=num%3
        test3=num%5
        test4=num%7
        test5=num%11 #Teste dos números primos do 2 ao 11.

        if num==11: 
            print("11","\n7","\n5","\n3","\n2")
            break
        elif num==10 or num==9 or num==8 or num==7:
            print("7","\n5","\n3","\n2")
            break
        elif num==5:
            print("5","\n3","\n2")
            break
        elif num==3:
            print("\n3","\n2")
            break
        elif num==2: #Caso os números digitados sejam do 2 ao 11. Ele já imprime os primos que estão nas variáveis de testes.
            print(2)
            break
        elif test1==0 or test2==0 or test3==0 or test4==0 or test5==0: #Testa números acima de 11. Caso o resto dos testes seja 0, o número não é imprimido.
            num=num-1
            continue
        elif test1!=0 and test2!=0 and test3!=0 and test4!=0 and test5!=0: #Testa números acima de 11. Caso o resto dos testes seja 0, o número é imprimido.
            print(num)
            num=num-1
            continue
def feature52():
    vogal=input("digite uma palavra: ") 
    print(vogal.count("a")+(vogal.count("e")+(vogal.count("i")+(vogal.count("o")+(vogal.count("u")))))) #contar quantas vogais existem na palavra
    print(vogal)
def feature53():
    print("")
def feature54():
    print("")
def feature55():
    print("")
    print("")

