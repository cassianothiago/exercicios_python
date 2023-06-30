from getpass import getpass
senha=getpass(input('digite: '))
confirme=getpass(input('confirme: '))
if senha==confirme:
    print('correto')
else:
    print('errado')
