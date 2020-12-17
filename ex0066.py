print("""
Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
""")

contador =0
soma=0
while True:
    n=int(input('digite um numero: '))
    if n == 999:
        break
    contador = contador +1
    soma = soma + n
print(f'a soma dos {contador} valores é igual a {soma} !')