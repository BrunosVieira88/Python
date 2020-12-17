print("""
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
""")
continuar= 's'
maior=0
menor=0
total=0
c=0
while continuar != 'n':
    n=int(input('Digite um numero: '))

    total = total + n
    c = c + 1
    continuar=str(input('voce quer continuar?[s/n]')).lower()

    if c == 1 :
        maior = n
        menor = n

    else:
        if n > maior:
           maior= n
        elif n < menor :
            menor= n

print('o numero de valores lidos foi {} '.format(c))
print('o maior valor lido é igual a {} '.format(maior))
print('o menor valor lido é igual a {} '.format(menor))
print(' a media dos valores lidos foi {:.2f} '.format(total/c))


