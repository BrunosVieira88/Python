from random import randint
from time import sleep
print(""""
ESCOLHA
PEDRA   [0]
PAPEL   [1]
TESOURA [2]
""")
jogador=int(input('Digite sua escolha: '))
computador=randint(0,2)
itens=('pedra','papel','tesoura')



print('\033[36mJO\033[m')
sleep(1)
print('\033[31m      KEN\033[m')
sleep(1)
print('\033[33m              PO\033[m')
sleep(1)

if jogador ==0 and computador ==0:
    print('EMPATE voce escolheu {} e o computador {}'.format(itens[jogador],itens[computador]))
elif jogador ==0 and computador ==1:
    print('Voce PERDEU voce escolheu {} e o computador {}'.format(itens[jogador],itens[computador]))
elif jogador ==0 and computador ==2:
    print('voce GANHOU voce escolheu {} e o computador {}'.format(itens[jogador],itens[computador]))
elif jogador ==1 and computador ==0:
    print('voce GANHOU voce escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
elif jogador ==1 and computador ==1:
    print('EMPATE voce escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
elif jogador ==1 and computador ==2:
    print('Voce PERDEU voce escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
elif jogador ==2 and computador ==0:
    print('voce GANHOU voce escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
elif jogador ==2 and computador ==1:
    print('Voce PERDEU voce escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
elif jogador ==2 and computador ==2:
    print('EMPATE voce escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
else:
    print(' se ta de sacanagem so tem 3 opçoes!!!',computador)

