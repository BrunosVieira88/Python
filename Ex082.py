lista=[]
pares=[]
impares=[]

while True:
    lista.append(int(input('Digite um numero')))
    continuar=str(input('Quer continuar [S/N]')).lower()
    if continuar == 'n':
        break


for i, v in enumerate(lista):
    if  v % 2 == 0:
        pares.append(v)
    else :
        impares.append(v)
print('A lista é :')
print(lista)
print(f'Os numeros impares sao {pares}')
print(f'Os numeros impares sao {impares}')