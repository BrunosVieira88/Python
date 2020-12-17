print("""
Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva
 para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
""")

from time import sleep

i = 10
for c in range (0,11):

    print(i)
    i = i - 1
    sleep(1)
print('\033[4;31mFeliz Ano Novo\033[m')