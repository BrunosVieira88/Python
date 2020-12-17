print(""""
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.
""")
i=int(input('digite um numero: '))
p=int(input('digite a Razão: '))
j=1
total = 0
for j in range (j,11):
    print('{}'.format(i),end='-> ')
    total = i + p
    i=total
print('ACABOU')