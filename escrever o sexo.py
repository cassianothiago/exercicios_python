print('='*120)
print("digite 'm' para masculino, 'f' para feminino e 'o' para outros")
a=(input('entre com a letro do sexo: '))

if a=='m' or a=='M':
    print('sexo masculino')
elif a=='f' or a=='F':
    print('sexo feminino')
elif a=='o' or a=='O':
    print('sexo outros')
else:
    print('sexo invalido')
print('='*120)
