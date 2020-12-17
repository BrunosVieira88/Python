print("""Exercício Python 060: Faça um programa que leia um número qualquer
e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120""")

n1=int(input('Digite o numero que deseja saber o fatorial '))

c=n1
total=1
for c in range (c,0,-1):
    print('{}'.format(c),end='')
    print(' X ' if c > 1 else '= ', end='')
    total = total*c

print(total)