import math
print("""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de 
R$50, R$20, R$10 e R$1.
""")
va=0
falta = 0
resta = 0
while True:
    print('{:-^40}'.format('Banco Brunão'))
    sacar = int(input('Quanto sera o valor do saque: '))
    print('***'*20)

    if falta != sacar :

          nota50 = sacar / 50
          total = 50 * math.floor(nota50)
          falta = falta + total
          resta = resta +(sacar -total)


    if nota50 >= 1:
                print(f'voce recebera {math.floor(nota50)} notas de 50 RS')

    if  falta == sacar:
                break
    if falta != sacar :
              nota20 = resta / 20
              total = 20 * math.floor(nota20)
              falta = falta + total
              resta = resta- total

    if nota20 >= 1:
         print(f'voce recebera {math.floor(nota20)} notas de 20 RS')

    if falta == sacar:
                    break
    if falta != sacar :
              nota10 = resta / 10
              total = 10 * math.floor(nota10)
              falta = falta + total
              resta = resta- total
    if nota10 >= 1:
              print(f'voce recebera {math.floor(nota10)} notas de 10 RS')


    if falta == sacar:
            break
    elif falta != sacar:
        nota2 = resta / 2
        total = 2 * math.floor(nota2)
        falta = falta + total
        resta = resta - total

    if nota2 >= 1:
        print(f'voce recebera {math.floor(nota2)} notas de 2 RS')



    if falta == sacar:
        break



