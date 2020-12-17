from random import shuffle

a=str(input('digite o primeiro '))
b=str(input('digite o segundo '))
c=str(input('digite o terceiro '))
d=str(input('digite o quarto '))

lista = [a,b,c,d]
shuffle(lista)
print ('a ordem de apresentação será {}'.format(lista))