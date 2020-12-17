print("""Exercício Python 053: Crie um programa que leia uma frase qualquer
 e diga se ela é um palíndromo, desconsiderando os espaços.""")

nome=str(input('Digite uma frase: ')).strip().lower()
recebe=nome.split()
junto=''.join(recebe)
novonome=''
for letra in range (len(junto)-1,-1,-1):
    novonome =novonome+ junto[letra]

if junto == novonome:
    print('a frase {} é um Palindromo'.format(novonome))
else:

    print('A frase {} ao contrario  {} não forma um PALINDROMO '.format(nome,novonome))