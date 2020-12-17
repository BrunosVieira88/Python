print("""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.""")


numero=[]
terminou=''




while terminou != 'n' :
    numero.append(int(input("Digite um numero")))
    terminou =str(input('Quer continuar [S/N]')).lower()
    if terminou != 's':
        while terminou != 's' and terminou !='n':
            terminou = str(input('Quer continuar [S/N]')).lower()

print(f'A lista tem {len(numero)} de elementos')
numero.sort(reverse=True)
print('Os numeros em ordem decresente são ')
for i in range (0,len(numero)):
    print( numero[i],end=" ")
if 5 in numero :
     print('\nExite o numero 5 na lista' )
else:
    print('\nNao tem cinco na lista ')
