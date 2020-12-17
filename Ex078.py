print("""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """)



lista=[]
cont = 0

for i in range (0,5):
    lista.append(str(input("digite um numero ")))

    cont += 1
    if cont == 1 :
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior :
            maior = lista[i]
        if lista[i] < menor:
            maior = lista[i]

for i in range (0,5):
    print(lista[i], end= " ")
print(f'\nO maior numero é {maior}')
print(f'O menor numero é {menor}')