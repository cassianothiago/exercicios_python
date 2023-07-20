''''4.	Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''


list_numero=[1,2,3,4,5,6,7,8,9,10]
list_altura=[157,160,170,191,183,174,187,164,153,175]

baixo=min(list_altura)
print('Altura minima = ',baixo)
alto=max(list_altura)
print('Altura maxima = ',alto)
encont_baixo=list_altura.index(baixo)
encont_alto=list_altura.index(alto)


print('Altura minima -{}cm- é do aluno numero -{}-'.format(baixo,list_numero[encont_baixo]))
print('Altura maxima -{}cm- é do aluno numero -{}-'.format(alto,list_numero[encont_alto]))