#2.	Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
print('='*120)

a=input('crie um nome de usuário: ')
b=input('crie uma senha: ')
while a==b:
    print('Nome do usuário não pode ser igual a senha. Digite novamente!')
    a=input('nome do usuário: ')
    b=input('senha do usuário: ')
print('='*120)
print(a)
print(b)
print('='*120)
