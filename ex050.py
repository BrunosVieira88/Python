print("""
Exercício Python 050: Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


""")

i=1
t=0
v=0

for i in range (i,7):
    n=int(input('digite o {}º numero :'.format(i)))
    if n %2 ==0:
        t= t+n
        v= v+1

if  v > 1:
  print('o valor total de {} numeros pares que somados é igual a {} '.format(v,t))
elif v == 1:
    print('voce digitou apenas {} numero par que foi {}'.format(v,t))
else :
  print('voce nao digitou numeros pares')