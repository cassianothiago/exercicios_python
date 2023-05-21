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
        print('A temperatura de {}º Celsius é iqual a {}º Fahrenheit'.format(temp,f))
        print('='*55)
        print('Obrigado por usar o conversor de temperatura')
    elif a==2:
        temp=float(input('Digite a temperatura em Fahrenheit: '))
        c=(temp-32)/1.8
        print('A temperatura de {}º Fahrenheit é iqual a {}º Celsius'.format(temp,c))
        print('='*55)
        print('Obrigado por usar o conversor de temperatura')
    else:
        print('Número digitado inválido. Favor digitar 1 ou 2 ou 0!')      
    os.system('pause')
    os.system('cls')
print('='*120)
