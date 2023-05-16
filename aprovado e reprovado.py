print('='*120)
a=float(input('digite a primeira nota: '))
b=float(input('digite a segunda nota: '))
media=(a+b)/2
if media>=7.0:
    print('média = %.2f Aprovado'%media)
elif media>5.0 and media<=6.99:
    print('média = %.2f Recuperação'%media)
else:
    print('média = %.2f Reprovado'%media)
print('='*120)
