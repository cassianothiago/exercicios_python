import os
while True:
    print('='*200)
    print('======== Calculadora em python =========')
    a=int(input('digite 1 para soma 2 para divisão 3 para multiplicação 4 para subtração 5 para volume do cubo 6 para potenciação 7 para raiz 8 para area do quadrado 9 para media e 10 para fatorial ou zero para sair: '))
    print('='*200)
    if a==1:
        print('bem vindo a soma')
        soma1=float(input('digite o primeiro numero: '))
        soma2=float(input('digite o segundo numero: '))
        soma_total=soma1+soma2
        print(soma_total)
    elif a==0:
        print('obrigado por usar a calculadora')
        break
    elif a==2:
        print('bem vindo a divisão')
        div1=float(input('digite o primeiro numero: '))
        div2=float(input('digite o segundo numero:'))
        div_total=div1/div2
        print(div_total)
    elif a==3:
        print('bem vindo a multiplicação')
        mult1=float(input('digite o primeiro numero: '))
        mulit2=float(input('digite o segundo numero: '))
        mult_total=mult1*mulit2
        print(mult_total)
    elif a==4:
        print('bem vindo a subtração')
        sub1=float(input('digite o primeiro numero: '))
        sub2=float(input('digite o segundo numero: '))
        sub_total=sub1-sub2
        print(sub_total)
    elif a==5:
        print('bem vindo ao volume do cubo')
        aresta=int(input('digite a aresta do cubo: '))
        volume=aresta**3
        print(volume)
    elif a==6:
        print('bem vindo a potenciação')
        base=int(input('digite a base: '))
        exp=int(input('digite o expoente: '))
        pot=base**exp
        print(pot)
    elif a==7:
        print('bem vindo a raiz quadratica')
        raiz=float(input('digite o numero: '))
        r=(1/2)
        squad=raiz**r
        print(squad)
    elif a==8:
        print('bem vindo a area do quadrado')
        lado=int(input('digite o lado do quadrado: '))
        area=lado**2
        print(area)
    elif a==9:
        print('bem vindo a media')
        m1=float(input('digite o numero: '))
        m2=float(input('digite o numero: '))
        m3=float(input('digite o numero: '))
        m4=float(input('digite o numero: '))
        media=(m1+m2+m3+m4)/4
        print(media)
    else:
        print('bem vindo ao fatorial')
        fat=int(input('digite o numero: '))
        cont=1
        z=1
        while cont<fat:
            cont=cont+1
            z=cont*z
        print(z)
    os.system('pause')
    os.system('cls')
    print('='*200)    
