def digitos():
    a=int(input('digite o numero: '))
    x=str(a)
    if x==0:
        x=int(a)
    print(len(x))
    

#print('quantidade de digitos')
#digitos()

def achaTamanho(x):
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)


num = int(input("Digite um número: "))
print(achaTamanho(num))

