def numero():
    num=int(input('digite um numero: '))
    if num>0:
        print('o numero digitado é Positivo')
    elif num<0:
        print('o numero digitado é Negativo')
    else:
        print('o numero é zero')
    return 'proximo numero'
print('calculadora de numero positivo negativo ou zero')
while True:
    a=numero()
    print(a)
