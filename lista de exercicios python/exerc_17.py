#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500
cont=0
ult=1
pen=1
n=500
print(1)
print(1)
while cont<n-2:
    cont=cont+1
    prox=ult+pen
    ult=pen
    pen=prox
    print(prox)
    soma=prox+ult
    if soma>=500:
        break
