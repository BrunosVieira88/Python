from datetime import date
print("""'
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
""")


demaior = 0
demenor = 0
for i in range(1,8):
        idade=int(input('O ano de nascimento do {}º entrevistado'.format(i)))
        atual =date.today().year
        idade = atual-idade
        if idade > 18 :
            demaior= demaior+1
        else :
            demenor= demenor+1
print('existem {} pessoas de MENOR e {} pessoas de MAIOR'.format(demenor,demaior))