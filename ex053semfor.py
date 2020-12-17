print("""Exercício Python 053: Crie um programa que leia uma frase qualquer
 e diga se ela é um palíndromo, desconsiderando os espaços.""")

nome=str(input('Digite uma frase: ')).strip().lower()
recebe=nome.split()
junto=''.join(recebe)
novonome=junto[::-1]

'''novonome=''
for letra in range (len(junto)-1,-1,-1):
    novonome =novonome+ junto[letra]'''

if junto == novonome:
    print('a frase\033[31m {}\033[m é um Palindromo'.format(nome))
else:

    print('A frase \033[31m{}\033[m ao contrario  \033[31m{}\033[m não forma um PALINDROMO '.format(nome,novonome))