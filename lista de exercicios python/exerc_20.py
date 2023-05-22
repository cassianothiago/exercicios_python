#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
print('='*120)
soma=0
lista=[]

while True:
    num=int(input('digite os numeros que deseja somar e digite zero para ver o resultado da soma: '))
    soma=soma+num
    lista.append(num)
    if num<0 or num>1000:
        num=int(input('digita apenas numeros entre 0 e 1000: '))
    elif num==0:
        lista.remove(0)
        ret=list(filter(lambda num:num>0,lista))
        print('numeros= '+str(ret))
        print('a soma dos numeros digitados é {} o menor valor é {} e o maior é {}'.format(soma,min(ret),max(ret)))
        break
print('='*120)
