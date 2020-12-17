print("""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
""")
n=(int(input('Digite um numero')),
   int(input('Digite um numero')),
   int(input('Digite um numero')),
   int(input('Digite um numero')))
print('#'*20)
print(f'O numero nove aparece {n.count(9)} vezes')
if 3 in n :
    print(f'o numero tres aparece na {n.index(3)+1} posição')
    print('os valores pares são: ', end='')
else :
    print('não ha numero 3 na lista')
    print('os valores pares são: ',end='')
for i in range (0,4):
    if n[i] % 2 == 0 :
        print(f'{n[i]}  ',end='')
