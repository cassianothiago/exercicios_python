def verificar_numero():
    print("\nBem vindo a verificação de números")
    num = int(input("Digite um número: "))
    if num == 0: # Condição onde o número digitado for igual a "0" irá imprimir ("O número digitado foi zero")
        print("\nO número digitado foi zero.\n")
    elif num < 0: # Condição onde o número digitado for menor que "0" irá imprimir ("O número digitado é negativo")
        print("\nO número digitado é negativo.\n")
    else: # Condição onde o número digitado for menor que "0" irá imprimir ("O número digitado é positivo")
        print("\nO número digitado é positivo.\n")      
        
def calcular_media():

    print("*",64*"-","*")
    print("|",64*" ","|")
    print(("|"+13*" "+"Seja bem vindo a Media de três numeros!!"+13*" "+"|")) # quadro mostrando 'seja bem vindo'
    print("|",64*" ","|")
    print("*",64*"-","*")
    print()
    num1 = float(input("Digite o primeiro numero: ")) # numero um para calculo
    num2 = float(input("Digite o segundo numero:  ")) # segundo numero para calculo
    num3 = float(input("Digite o terçeiro numero: ")) # terceiro numero para calculo
    soma = ((num1+num2+num3)/3)  # soma dos três numeros e dividido por 3 
    print("\nA media dos três numeros é: %.0f"% soma)  # mostra da do resultado
    print("\nObrigado pela preferencia...\nVolte sempre\n") # sendo simpatico, com volte sempre

def verificar_ano_bissexto():

    print("=====SEJA BEM VINDO=====")#essa funçao da boas vindas
    ano=int(input("digite um ano:"))
    if ano % 4==0 and ano % 100 !=0 or ano % 400==0:#essa funçao vai faz os calculos
     print("ess ano e bissexto.".format(ano))
    else:
      print("esse ano nao e bissexto.".format(ano))
    print("=====MUITO OBRIGADO=====")#essa funçao da agradecimento 


def converter_nota_letra():
    
  while True:
     op=input(" Digite 1 para continuar ou 0 para sair:")# para continuar coloco o 1 e para sair é o 0.
     if op=="0":
         print(" Saindo...")
         print("** Obrigada por usar o programa, volte sempre! ** ")# para sair o usuário digita 0 e o programa encerra, se despedindo.
         break
     
     elif op=="1":
      print(" <<<<<<< Bem vindo ao ミ★ Sistema de Notas ★彡!>>>>>>") 
      # boas vindas!, SE a pessoa digitar números negativos, ou maior que 100, ele imprime "Nota inválida! Por favor digite uma nota de 0 a 100!""
     notas=float(input("<<<<<<  Por favor, digite uma nota de 0 a 100: >>>>>>>\n✎ :"))# pedir para o usuário digitar uma nota de 0 a 100.
    # Começa os elementos de condições, 
    # ou seja os testes para ver se a condição é verdadeira ou falsa.
     if notas >-1 and notas<60:# para o código pegar o número 0 e mostrar como F, tive que colocar -1 e menor que 60
            print(">>>> Nota F!")# ele imprime f de falhou.

     elif notas>=60 and notas<=62:# se a primeira  condição(o IF)for falsa, ele irá para a segunda condição que é o senão.
            print(">>>> Nota D-") #ele ira ver se nota é maior ou igual a 60 e 62, se for ele imprime nota D- que é pouco suficiente.
    
     elif notas>=63 and notas<=66:# para entrar nessa tem que colocar >="número" and <="número"
            print(">>>> Nota D")# se for esse , ele imprime o D de pouco suficiente.

     elif notas >=67 and notas<=69:# em todas as condições está >="numero" and <="numero" para que ele entre na condição.
            print(">>>> Nota D+")# ele irá imprimir D+ de pouco suficiente.

     elif notas >=70 and notas<=72:# em todas as condições está >="numero" and <="numero" para que ele entre na condição.
            print(">>>> Nota C-")# ele irá imprimir C- de pouco suficiente.

     elif notas>=73 and notas<=76:#se notas >=73 e <=76
            print(">>>> Nota C")# ele irá imprimir c de suficiente.

     elif notas >=77 and notas<=79:#se notas >=77 e notas<=79
            print(">>>> Nota C+")# ele irá imprimir C+ de média.

     elif notas >=80 and notas<=82: # se notas >=80 e <=82
            print(">>>>. Nota B-") # ele irá imprimir B- de bom

     elif notas >=83 and notas<=86: # se notas >=83 e <=86
            print(">>>> Nota B") # ele irá imprimir B de bom

     elif notas >=87 and notas<=89:# se notas >=87 e <=89
            print(">>>> Nota B+") # ele irá imprimir B+ de bom de mais

     elif notas >=90 and notas<=92:# se notas>=90 e <=92
            print(">>>> Nota A-") # ele irá imprimir A- de muito bom

     elif notas >=93 and notas<=96: # se notas>=93 e <=96
            print(">>>> Nota A")  # ele irá imprimir A de excelente   

     elif notas >=97 and notas<=100: # se notas >=97 e <=100
            print(">>>> Nota A+") # ele irá imprimir A+ de superior

     else:
        print("<<<< Nota inválida! Por favor digite uma nota de 0 a 100!>>>>")  #ESTÁ FUNCIONANDO ,Também mudei a ordem de algumas notas e letras no código, da imagem, explicando como são as notas.
        
        print("** Obrigado por ver a sua nota com a gente, volte sempre! **") 
     

def verificar_divisivel():
   print("MUAHAHAHAHAHAHAHA")
def encontrar_maior():
    print("="*39)
    print("------Bem Vindo ao Maior Número!-------")
    print("="*39)
    numeros = []#lista para receber todos os 4 números que vão ser digitados pelo usuario
    num_1 = float(input("|I Digite um número:\n  >> "))
    numeros.append(num_1)#Adiciona o 1º numero digitado pelo usuario a linsta "numero[]"
    print(">"+"-"*37+"<")
    num_2 = float(input("|I Digite outro número:\n  >> "))
    numeros.append(num_2)#Adiciona o 2º numero digitado pelo usuario a linsta "numero[]"
    print(">"+"-"*37+"<")
    num_3 = float(input("|I Digite outro número:\n  >> "))
    numeros.append(num_3)#Adiciona o 3º numero digitado pelo usuario a linsta "numero[]"
    print(">"+"-"*37+"<")
    num_4 = float(input("|I Digite outro número:\n  >> "))
    numeros.append(num_4)#Adiciona o 4º numero digitado pelo usuario a linsta "numero[]"
    maiornumero = max(numeros)#Analisa a lista "numeros[]", e encontra o maior numero que esta dentro da lista
    print("---------------Resultado---------------")
    print("             Maior número\n              >>",maiornumero,"<<")
    if num_1 == num_2 and num_2 == num_3 and num_3 == num_4:#se todos os numeros digitados pelo usario forem iguais, vai avisalo ao fim do programa
        print("Os números digitados são todos iguais!")
        print("-"*39)
    print("---Obrigado por usar o Maior Número!---")
    print("="*39)

def verificar_quadrado_perfeito():
    print("-----------------BEM VINDO----------------") 
    a=float(input("digite o primeiro lado do quadrado: ")) # pedindo o primeiro lado do quadrado
    b=float(input("digite o segundo lado do quadrado: ")) # pedindo o segundo lado do quadrado
    c=float(input("digite o terceiro lado do quadrado: ")) # pedindo o terceiro lado do quadrado
    d=float(input("digite o quarto lado do quadrado: ")) # pedindo o quarto lado do quadrado
    if a==b==c==d :  # se todos os numeros forem iguais
       print("O quadrado é perfeito!") # vai ler que o quadrado é perfeito
    else: # se nao for
      print("O quadrado é imperfeito!") # vai ler que o quadrado é imperfeito
    print("Obrigado!!!!!") 
        
def classificar_numeros():
    print("==========\nBem vindo - a - classificar - numeros\nEssa aplicação irá ordenar os números que você digitar em ordem decrescente\n==========")
    # este bloco, solicita ao usuario valores e os armazena nas variaveis numeros_xx
    numero_01 = float(input("Digite um número "))
    numero_02 = float(input("Digite um número "))
    numero_03 = float(input("Digite um número "))
    # este bloco utiliza os valores digitados pelo usuario e armazenados nas variaveis numeros_xx, e utiliza os condicionais para ordena-los de maneira decrescente
    if numero_01 > numero_02 and numero_02 > numero_03 :
        print("A classificação em ordem decrescente apartir dos números digitados é: ",numero_01,numero_02,numero_03)  
    elif numero_02 > numero_03 and numero_03 > numero_01 :
        print("A classificação em ordem decrescente apartir dos números digitados é: ",numero_02, numero_03, numero_01)
    elif numero_03 > numero_02 and numero_02 > numero_01 :
        print("A classificação em ordem decrescente apartir dos números digitados é: ",numero_03, numero_02, numero_01)
    elif numero_01 > numero_03 and numero_03 > numero_02 :
        print("A classificação em ordem decrescente apartir dos números digitados é: ",numero_01, numero_03, numero_02)
    elif numero_02 > numero_01 and numero_01 > numero_03 :
        print("A classificação em ordem decrescente apartir dos números digitados é: ",numero_02, numero_01, numero_03)
    elif numero_03 > numero_01 and numero_01 > numero_02 :
        print("A classificação em ordem decrescente apartir dos números digitados é: ",numero_03, numero_01, numero_02)
    print("==========\nObrigado!\n==========")

def verificar_multiplo():
    print("Bem Vindo a Verificação de Multiplos de 5 ou 7!!!!")#Escreve o Texto
    numero = int(input("Digite um número: "))#Input para receber o número
    resto = numero%5#Calcúlo para ver se é múltiplo de 5
    resto1 = numero%7#Calcúlo para ver se é múltiplo de 7
    if resto == 0:
        print("O número %d é multiplo de 5!!!"%numero)#Se resto for 0 é multiplo de 5
    if resto1 == 0:
        print("O número %d é múltiplo de 7!!!"%numero)#Se rest01 for 0 é multiplo de 7
    elif resto1 !=0 and resto !=0:
        print("O número %d não é multíplo de 5 nem de 7!!!"%numero)#Se resto não for zero encerra o progama
    print("\nObrigado por usar a calculadora de múltiplos de 5 ou 7!!!")

def verificar_palindromo():
    print("|-------------------------------------|")#a parte de seja bem vindo 
    print("|SEJA BEM VINDO AO TESTE DE PALINDROMO|")
    print("|-------------------------------------|")
    a = input("   Digite o numero ou Palavra: ")#aqui é pra pessoa digitar o numero ou palavra
    if str(a) == "".join(reversed(a)) :#a variavel vai ver se vai funcionar oque o usuario digitar
        print("A Palavra Digitada É um Palindromo")#aqui mostra se o numero digitado ou palavra é palindromo
    else:
        print("A Palavra Digitada Não é Palindromo")#aqui ja mostra se que a palavra ou numero digitado não é palindromo

def converter_temperatura():
    import os
    while True:
        print('='*120)
        print('======== bem vindo ao conversor de temperatura =========')
        a=float(input('Digite 1 para converter Celsus para Fahrenheit ou 2 para converter Fahrenheit para Celsius ou 0 para sair: '))
        print('='*120)
        if a==0:
            print('Obrigado por usar o conversor de temperatura')
            break
        elif a==1:
            temp=float(input('Digite a temperatura em Celsius: '))
            f=temp*1.8+32
            print('A temperatura de {}º Celsius é iqual a {:.2f}º Fahrenheit'.format(temp,f))
            print('='*55)
            print('Obrigado por usar o conversor de temperatura')
        elif a==2:
            temp=float(input('Digite a temperatura em Fahrenheit: '))
            c=(temp-32)/1.8
            print('A temperatura de {}º Fahrenheit é iqual a {:.2f}º Celsius'.format(temp,c))
            print('='*55)
            print('Obrigado por usar o conversor de temperatura')
        else:
            print('Número digitado inválido. Favor digitar 1 ou 2 ou 0!')      
        os.system('pause')
        os.system('cls')

def verificar_divisibilidade():
#Atividade avaliativa para saber se o numero e divisível por 4, mas não por 6
    
    print('================================================================================')
    print('=                                  Bem Vindo                                   =') 
    print('================================================================================')    
    num=int(input(' Por favor Digite um numero para ver se e  divisível por 4, mas não por 6: '))
    print('\n Você pode ver o resultado aqui em baixo !')                                     
    if num % 4 == 0 and num % 6 != 0:                                                         
            print('\n O numero e divisível por 4, mas não por 6: %d'%(num))                       
    else:                                                                                    
            print('\n o numero não atende ao criterio: %d'%(num))                                                                      
    print('================================================================================')
    print('=                              Obrigado Volte Sempre                           =') 
    print('================================================================================')

#para um numero ser divisível por 4 se os 2 ultimo numero e divisível por 4 exemplo 512,100,236
#agora alguns num que nao atende a esse criterio exemplo: 103,550,361
#Um número é divisível por 6 se for par e a soma de seus algarismos for divisível por 3.

def calcular_area_triangulo():
    print("----------------BEM VINDO! ÁREA DO TRIÂNGULO!----------------")
    base=float(input("Digite a base do triângulo: "))
    height=float(input("Digite a altura do triângulo: "))
    result=(base*height)/2
    print("A área do triângulo é {:.2f}".format(result))
        
def verificar_numero_armstrong():
    print("--------------- Bem vindo ---------------\n                   A\n------------Numero Armisthong ------------------\n")
    num =int(input("Digite um numero: ")) #=153
    tam = len(str(num))#=3
    soma = 0
    i=0
    while i <= tam-1 :
        n = int(str(num)[i])#esse ele pega a posição do numero do algoritimo ex153 ele pega o 5 na posição 1
        soma=soma+n**tam#esse pega o numero n ex 5*3 5*3 5*3 =126
        print(n**tam)#esse printa  5*3 5*3 5*3 =126
        i=i+1#esse soma sempre ms 1 na posição do algoritimo

    if num == soma:
        print("O número fornecido", num, "é o número de Armstrong")
    else:
        print("O número fornecido", num, "não é um número de Armstrong")
    print("Obrigado Por Participar")

def verificar_potencia_de_2():
    
    print("+"+"="*37+"+")
    print("|I"+" "*12+"\"Bem Vindo\""+" "*12+"I|")
    print("|I"+" \"A Verificação de Potências de 2\" "+"I|")
    print("+"+"="*37+"+")

    valor = int(input("I| Digite um Valor Inteiro: \n>> "))#Pedindo Valor ao Usúario.

    result = valor % 2 #Calculo para Saber o Resto da Divisão, se o Resto da Divisão for Igual á 0 é Potência de 2. 
                       #Caso o Contrario não é Potência de 2.
    if result == 0:
        print("+"+"="*37+"+")
        print("I| O Valor %d é Potência de 2"%valor)#Resultado da Operação.
        print("I| \"Obrigado por Utilizar esse Programa\"")
        print("+"+"="*37+"+")

    else:
        print("+"+"="*37+"+")
        print("I| O Valor %d não é Potência de 2"%valor)#Resultado da Operação.
        print("I| \"Obrigado por Utilizar esse Programa\"")
        print("+"+"="*37+"+")
     
def calcular_valor_absoluto():
    print("---------------------------------------------------------")
    print("|              Bem vindo ao Valor Absoluto!             |")
    print("---------------------------------------------------------")
    print("\n")
    print("Obs:O valor absoluto de um número é quantas casas existe entre ele e o 0.")
    print("\n")
    print("<--||--||--||--||--||--||--||--||--||-->")
    print("   -4  -3  -2  -1   0   1   2   3   4")

    n=float(input("Digite um número:"))
    if n>=0:
        print("O valor absoluto do número digitado é:")
        print(n)
    elif n<=0:
        print("O valor absoluto do número digitado é:")
        n=n*(-1) # aqui é onde transformamos o número negativo em seu valor absoluto, que é igual a ele mesmo sem sinal.
        print(n)
#calcular_valor_absoluto()

def verificar_triangulo_retangulo():

    #Verifique se três números podem formar um triângulo retângulo.

    print ("="* 38, "Bem-Vindo a Verificação do Triangulo Retangulo", "=" * 38)
    number1 = float(input("Digite o primeiro numero: ")) #Pedir o numero para vermos se eles irão se torna um Triangulo Retangulo
    number2 = float(input("Digite o segundo numero: "))
    number3 = float(input("Digite o terceiro numero: "))

    if number1 > number2 and number1 > number3: #Precisamos testa se o primeiro numero digitado é maior que os outros para entrar nessa condição
        hip = number1 #Caso entre nesta condição ele irão entrar dentro da variavel HIP
        if hip**2 == number2**2 + number3**2: #Entrando nessa condição utilizaremos Pitágoras para testarmos se os numeros digitados irão ser um triangulo (com o simbolo da == para testar se a hipotenusa é igual aos catetos)
             print ("\nÉ um triangulo retangulo!") #Caso seja verdade ele irá imprimir isto
        else: #Caso seja falso ele irá entrar neste ELSE para informar que o numero digitado não é um Triangulo Retangulo
             print ("\nNÃO é um triangulo retangulo")
    if number2 > number1 and number2 > number3:
        hip = number2
        if hip**2 == number1**2 + number3**2:
            print ("\nÉ um triangulo retangulo!")
        else:
            print ("\nNÃO é um triangulo retangulo")
    if number3 > number1 and number3 > number2:
        hip = number3
        if hip**2 == number2**2 + number1**2:
             print ("\nÉ um Triangulo Retangulo!")
        else:
             print ("\nNÃO é um Triangulo Retangulo")
 
def determinar_raizes():
    lista=[]
    print('-'*60)
    print('           --- Bem Vindo a Equação Quadrática ---')
    print('-'*60)
    a=int(input('                  Informe o valor de a:'))
    b=int(input('                  Informe o valor de b:'))
    c=int(input('                  Informe o valor de c:'))

    while True:
        delta = b**2 - 4*a*c #calcula valor de delta
        if delta < 0: #se o numero for negativo, ñ possui raiz real
            print('                  Não possui raízes reais')
            break
        else:
            x1 = (-b - delta**0.5) / 2*a #descobre o primeiro valor da equação
            x2 = (-b + delta**0.5) / 2*a #descobre o segundo valor da equação

            lista.append(x1) # coloca os valores dentro da lista
            lista.append(x2)

            print('           O maior número da equacação é:',end='')
            print(max(lista)) # pega o número maior dentro da lista
            print('           O menor número de uma equação é:',end='')
            print(min(lista)) # pega o número menor dentro da lista
            break
    print('-'*60)
    print('       Obrigado por usar Equação Quadrática Conosco!!')
    print('-'*60)
        
def calcular_raiz_cubica():
    print ("="*50)
    print ("|      Bem Vindo ao Cálculo de Raiz Cúbica       |")# A raiz cúbica é uma radiciação com índice igual 3
    print ("="*50)
    numero = float(input("| Informe o valor desejado: "))
    if numero >= 0:
        raizC = numero ** (1/3) # Realiza o cálculo da raiz cúbica de um número (n³ = b) 
        print ("| A raiz cúbica de %.1f é de %.1f" % (numero, raizC))# Imprimir o número digitado e o seu resultado
    else: 
        print ("| Número inválido")
    print ("="*50)
    print ("|                Obrigado por usar!              |")
    print ("="*50)

def calcular_desconto():
    print("!!!!!!!!!!!!!!!!!} BEM VINDO --- COMPRA E DESCONTO {!!!!!!!!!!!!!!!!!!!!")
    val=float(input("Digite o valor total da compra: ")) #Pede o valor total da compra.
    desc=float(input("Porcentagem de desconto: ")) #Pede a taxa de porcentagem.
    desc1=desc/100 #Divide essa taxa de porcentagem por 100 e a atribui a uma nova variável.
    result=val-(val*desc1) #Realiza o cáculo de desconto.
    print("Valor Inicial do produto: {:f}\nTaxa de Desconto: {:f}\nValor Final com desconto: {:.2f}".format(val,desc,result)) #Imprime os resultados.
def classificar_numeros():   
    list=[]    
    while True:
        op=int(input("BEM VINDO À ORDENAÇÃO CRESCENTE, DIGITE 3 VALORES E EU OS COLOCAREI EM ORDEM CRESCENTE!!!\n\nDigite 1 para continuar ou 0 para sair do programa: "))
        if op==1:
            num1=int(input("\nValor 1: "))
            num2=int(input("Valor 2: "))
            num3=int(input("Valor 3: "))
            list=[num1,num2,num3]
            list.sort(reverse=False)
            print(list)
        elif op==0:
            print("OBRIGADO POR USAR O PROGRAMA!!!")
            break
        else:
            print("VALOR INVÁLIDO, TENTE NOVAMENTE!!\n\n")


       
def calcular_area_circulo():
    print("MUAHAHAHAHAHAHAHA")
    print("-------BEM VINDO-------")
    r= float(input("Qual o raio do círculo? \n"))
    area= (3.14*r*r)
    print("A área do círculo é igual a ",(area))
    print('------OBRIGADO------')

def calcular_produto_escalar():
    #Programa para calcular o produto escalar dos vetores
    print("--------------------Bem vindo ao calculo do produto escalar de vetores!--------------------\n")
    print("                                         Vamos começar!\n")
    print("                 Dados os vetores V (v1,v2,v3) e W (w1,w2,w3) adicione os valores para calcular o produto escalar!\n")
    while True: 
        print("--Adicione os valores do vetor V (v1,v2,v3):") #Pedido para adiconar os vetores V
        vetorv1=int(input("Digite o valor do v1: "))
        vetorv2=int(input("Digite o valor do v2: "))
        vetorv3=int(input("Digite o valor do v3: "))
        print("--Agora adicione os valores do vetor W (w1,w2,w3):")#Pedido para adicionar os vetores W
        vetorw1=int(input("Digite o valor do w1: "))
        vetorw2=int(input("Digite o valor do w2: "))
        vetorw3=int(input("Digite o valor do w3: "))
        break
    resul_prodVet=((vetorv1*vetorw1)+(vetorv2*vetorw2)+(vetorv3*vetorw3)) #Calculo dos produtos dos vetores
    print("V(%d, %d, %d) x W(%d, %d, %d) = %d \n"%(vetorv1,vetorv2,vetorv3,vetorw1,vetorw2,vetorw3,resul_prodVet))
    print("  --------------------OBRIGADO POR CALCULAR COM A GENTE!--------------------  ")
    
def calcular_media_ponderada():
    print("-----------Seja bem vindo ao calculador de média ponderada-----------") #Boas vindas
    print("Digite sua primeira nota: ") #pede a primeira nota
    A = float(input())                  #Armazena a primeira nota
    print("Digite sua segunda nota: ")  #Pede a segunda nota    
    B = float(input())                  #Armazena a primeira nota
    print("Digite sua terceira nota: ") #Pede a terceira nota
    C = float(input())                  #Armazena a primeira nota
    media = ((A*3)+(B*4)+(C*5))/(3+4+5) #Pesos das medias são 3, 4 e 5 para cada respectiva nota
    print("Sua média ponderada foi de  = %.2f" % media) #Exibe a média ponderada
    print("-----------Muito obrigado-----------") #Agradecimento

def calcular_raiz_quadrada():
    import os
    while True :
        print('====Bem vindo ao cálculo da raiz quadrada====')
        raiz=int(input('digite o numero para calcular sua raiz quadrada ou zero para sair: '))
        if raiz>0:
            calc=raiz**(1/2)
            print('A raiz quadrada de {} é {} '.format(raiz,calc))
        elif raiz<0:
            print('A raiz não pode ser negativa')
        else:
            break
        os.system('pause')
        os.system('cls')
        
def verificar_triangulo_equilatero():
    
    print("----------BEM VINDO----------\n             A\n       VERIFICAÇÃO DE\n    TRIANGULO EQUILATERO\n-----------------------------")
    num1=float(input("Digite o numero do lado1: "))
    num2=float(input("Digite o numero do lado2: "))
    num3=float(input("Digite o numero do lado3: "))

    while True:
        if num1==num2 and num2==num3:
            print("Esse é um triangulo equilátero")
       
        else :
            print("Esse Triangulo nao é Equilátero")      

        print("Obrigado por participar.")
        break

def sequencia_fibonnacci():
    print ("="*95)
    print ("="*100)
    print ("!              B O A S - V I N D A S   A   S E Q U Ê N C I A   D E   F I B O N N A C C I           !") 
    print ("="*100)
    print ("\n")

    n = int(input('Qual número deseja pra ser a sequência: '))#Input pro usuário colocar o número de seu interesse
    a, b = 0, 1
    while a < n:
        print(a,  end=' , ')#A base pra mostrar os números
        a, b = b, a+b #Fazendo as somas para que a sequência possa ser realizada

    print ("\n")
    print ("="*100)
    print ("!                             O B R I G A D O   P O R   U S A R                                    !")
    print ("="*100)
