print("""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """)

numeros=[]
fim = ""
while fim != "n":
    n=int(input("digite um numero"))
    if n not in numeros :
        numeros.append(n)
        fim = str(input("quer continuar ? [ S/N ]")).lower()
    else:
        print('numero repetido')

numeros.sort()
for i in range(0,len(numeros)):
    print(numeros[i],end= " ")
