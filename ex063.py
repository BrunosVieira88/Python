print("""
Exercício Python 063: Escreva um programa que leia um número N 
inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
""")
a = 0
b = 1
total=0
n=int(input('digite quantos elementos ha na sequencia de Fibonacci: '))
c=1
print('{} -> {} -> '.format(a,b),end='')
while c < n :
  f = a + b
  print('{}-> '.format(f),end='')
  a=b
  b=f
  c = c +1
print('FIM')