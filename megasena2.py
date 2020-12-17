from random import randint

sorteados=[]
jogados = []
cont =0
cont2=0
cont3=0

while cont3 != 6:
    numero=randint(1,60)
    if numero not in sorteados:
        sorteados.append(numero)
        cont3 += 1

print('-'*50)
print(f'{"MEGA SENA":^50}')
print('-'*50)

while cont2 != 6:
     j=int(input("Digite seu jogo"))
     if j <=60:
        jogados.append(j)
        cont2 += 1
     else:
        print('Digite um valor valido')
for i in range (0,6):
    if jogados[i] in sorteados:
      cont += 1
print('OS NUMERO SORTEADOS FORAM:')
for i in range (0,6):
    sorteados.sort()
    print(sorteados[i], end= " ")

if cont == 6:
    print('\nVOCE GANHOU É UM MILIONARIO')
    for i in range(0,6):
        print(f'{jogados[i]}',end =" ")
else:
    print('\nVOCE PERDEU CONTINUE TENTANDO ')
    for i in range(0, 6):
        print(f'{jogados[i]}',end=" ")
print(' Seu jogo')
