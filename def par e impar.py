def par(x):
    if x%2==0:
        return True
    else:
        return False
while True:
    num=int(input('digite o numero: '))
    if par(num):
        print(num,'é par')
    else:
        print(num,'é inpar')
