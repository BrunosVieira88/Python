print("""
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
""")
soma=0
c=0
parada = 0
while parada != 999:
    n = int(input('didgite um numero [999 para a operaçao]'))
    if n == 999:
        parada = n
    else:
         soma = soma + n
         c = c +1
print('a soma dos numeros é igual a {}'.format(soma))
print('voce digitou {} numeros'.format(c))