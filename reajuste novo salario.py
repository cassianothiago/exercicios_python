print('='*120)
a=float(input('digite seu salario: '))

if a<500.00:
    reaj=a+(a*15/100)
    print('seu salario de R$ {:.2f} foi aumentado em 15% e seu novo salario é R$ {:.2f}'.format(a,reaj))
elif a>=500.00 and a<1000.00:
    reaj=a+(a*10/100)
    print('seu salario de R$ {:.2f} foi aumentado em 10% e seu novo salario é R$ {:.2f}'.format(a,reaj))
else:
    reaj=a+(a*5/100)
    print('seu salario de R$ {:.2f} foi aumentado em 15% e seu novo salario é R$ {:.2f}'.format(a,reaj))
print('='*120)

