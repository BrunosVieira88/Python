print("""
Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.

""")
v=0
i=1
t=0
for i in range(i,500):
    if i %2 != 0 and i %3 == 0:
        v=v+i
        t= t+1
print('a soma de {} valores é igual a {}'.format(t,v))
