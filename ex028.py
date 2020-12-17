from random import randint
from time import sleep
var=randint(0, 5)
print('*---*'*10)
print ('Chute um numero entre 0 e 5')
print('-----'*10)
num=int(input('digite um numero'))
print('PROCESSANDO')
sleep(1)
print('.')
sleep(1)
print('..')
sleep(1)
print('...')


if num == var :
    print('voce GANHOU o numero pensado foi {} o mesmo que voce jogou {var}')

else:
    print ('voce PERDEU o numero pensado foi {} e nao o jogado {}'.format(var,num))