print("""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
""")
from random import randint
numeros=('','','')
n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('*' * 30)
print('Os numeros sorteados são !')
for i in range(0,5):

   print(n[i], end=' ')

   if i == 0 :
       maior = n[i]
       menor = n[i]
   if n[i] <= menor:
        menor=n[i]
   if n[i]>=maior:
        maior=n[i]

print('\n')
print('*'*30)
print(f'O maior valor nessa lista é {maior}')
print(f'O menor valor nesta lista é {menor} ')
print('*'*30)
print(f'\n {max(n)}')
print(f'\n {min(n)}')