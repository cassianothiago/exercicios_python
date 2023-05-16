print('='*120)
idade=18
if idade<20:
    print('vc é jovem')
print('fora do if')
print('='*120)

idade=int(input('digite sua idade: '))
if idade>18:
    print('maior de idade')
else:
    print('menor de idade')
print('='*120)

idade=int(input('digite sua idade: '))
if idade==16:
    print('pode votar')
else:
    if idade>=16:
        print('pode dirigir')
    else:
        if idade<16:
            print('apenas estude')
print('='*120)

idade=int(input('digite sua idade: '))
if idade>=16 and idade<16:
    print('pode votar')
elif idade<16:
    print('só estude')
else:
    print('pode votar e dirigir')
print('fim')
print('='*120)
