print(""""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
""")

entrada = 0


while entrada != 5 :

    n1 = int(input('digite o primeiro numero '))
    n2 = int(input('digite o segundo numero '))
    entrada=int(input('digite a função desejada: '))
    if entrada == 1:

        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif entrada == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif entrada == 3:
       if n1>n2:
           print('{} é maior que {}'.format(n1,n2))
       else:
           print('{} é maior que {}'.format(n2,n1))
    elif entrada == 4 :
        n1 = float(input('digite o primeiro numero '))
        n2 = float(input('digite o segundo numero '))

