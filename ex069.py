from time import sleep
print("""
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
 No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
""")
a =0
homem = 0
mulher=0
while True:
    print('*-'*20)
    idade=int(input('Digite sua idade: '))
    sexo= str(input('digite seu sexo:')).lower().strip()
    if sexo != 'm' and sexo != 'f':
        print('voce nao digitou um valor valido ')
    print('*-' * 20)
    continuar= str(input('quer continuar[S/N]')).lower().strip()

    if idade >= 18:
        a = a + 1
    if sexo == 'm':
        homem = homem + 1
    if sexo == 'f' and idade <= 20:
        mulher = mulher + 1


    if continuar != 's' and continuar != 'n':
        print('voce nao digitou um valor valido ')

    if continuar == 's':
        print('novo cadastro')

    elif continuar == 'n':
        print('F')
        sleep(1)
        print('I')
        sleep(1)
        print('N')
        sleep(1)
        print('A')
        sleep(1)
        print('L')
        sleep(1)
        print('I')
        sleep(1)
        print('Z')
        sleep(1)
        print('A')
        sleep(1)
        print('N')
        sleep(1)
        print('D')
        sleep(1)
        print('O')

        break
print(f'existem {a} pessoas com mais de 18 !')
print(f'Existem {homem} homens cadastrados ')
print(f'Existem cadastrados {mulher} com menos de 20 !')