from random import randint
n1=int(input('digite um numero '))

sorteado=randint(0, 60)

if n1 == sorteado:
    print('parabens o numero {} que vc jogou foi o sorteado'.format(n1))

else:

    print('infelizmente o numero {} que vc jogou nao foi o sorteado'.format(n1))
    print('o numero sorteado foi {}'.format(sorteado))