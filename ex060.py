print("""Exercício Python 060: Faça um programa que leia um número qualquer
e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120""")


n1 = int(input('Digite um numero para descobrir seu fatorial'))
contador= n1
total=1


print('calculando {}!  = '.format(n1),end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' X ' if contador > 1  else '=' , end='')
    total= total *contador
    contador = contador - 1





print(' {}'.format( total))