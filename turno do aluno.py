print('='*120)
a=input('digite o seu turno. M-matutino, V-vespertino e N-noturno: ')
a=a.capitalize()
print('='*120)
if a=='M':
    print('bom dia aluno')
elif a=='V':
    print('bom tarde aluno')
elif a=='N':
    print('boa noite aluno')
else:
    print('turno invalido')
print('='*120)
