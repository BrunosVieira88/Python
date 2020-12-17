from random import randint
palpite =0
jogado =randint(0,11)
errado=0
while palpite != jogado :
        palpite=int(input('digite seu palpite: '))
        if palpite < jogado:
            print( 'O numero é MAIOR')
        elif palpite > jogado:
            print('o numero é MENOR')

        if palpite != jogado:
            errado = errado +1

        elif jogado == palpite and errado >=1:
            print('-----'*10)
            print('voce Errou {} vezes \n '.format(errado),end='')

print('ACERTOU o numero pensado foi {} '.format(jogado))
print('-----'*10)