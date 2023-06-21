def conversao_horas(hora,minuto):
    
    
    if hora<12:
        print(hora,':',minuto,'AM')
    if hora>=12:
        hora=hora-12
        print(hora,':',minuto,'PM')


print('conversão hora')
while True:
    hora2=int(input('digite a hora: '))
    minuto2=int(input('digite o minuto: '))
    conversao_horas(hora2,minuto2)
    a=input('tecle enter para continuar ou S para sair: ')
    if a=='s' or a=='S':
        break
    continue


        
    