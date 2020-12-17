from random import randint
print("""
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando 
o total de vitórias consecutivas que ele conquistou no final do jogo. 

""")
vitorias=0
c=0

while True:
    n=int(input('Digite um numero: '))
    var=str(input('voce quer Par ou impar: [P/I]')).lower()

    computador = randint(0,10)
    total= n + computador
    if var != 'p' and var != 'i':
         print('voce nao digitou um valor valido: \ntente novamente')

    if var  == 'p':
             if total % 2 == 0 :
                 print('*-' * 20)
                 print(f'voce jogou {n} computador jogou {computador}')
                 print(f'voce venceu {total} é par ')
                 print('*-' * 20)
                 c = c + 1
             else:
                 print('*-' * 20)
                 print(f'voce jogou {n} computador jogou {computador}')
                 print(f'voce errou {total} é impar!')
                 print('*-' * 20)
                 break

    if var == 'i' :
                    if total % 2 != 0 :
                        print('*-'*20)
                        print(f'voce jogou {n} computador jogou {computador}')
                        print(f'voce venceu {total} é impar ')
                        print('*-' * 20)
                        c = c + 1
                    else:
                        print('*-' * 20)
                        print(f'voce jogou {n} computador jogou {computador}')
                        print(f'voce errou {total} é par !')
                        print('*-' * 20)
                        break
print(f' voce acertou {c} vezes consecutivas  ')
