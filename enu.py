import enum
class Animal(enum.Enum):
    cachorro=1
    gato=2
    pantera=3
if Animal.cachorro is Animal.gato:
    print('cachorro=gato')
else:
    print('cachorro!=gato')

if Animal.pantera!=Animal.gato:
    print('leões!=gatos')
else:
    print('pantera=gatos')

    