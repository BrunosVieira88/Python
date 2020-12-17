print("""""
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
""")
media =0
contador=0
idademaior=0

for i in range (1,5):
            print('*'*20)
            print('----- {} PESSOA -----'.format(i))
            nome=str(input('NOME ')).strip()
            idade=int(input('IDADE '))
            sexo=str(input('SEXO [M] ou [F]')).lower()
            print('*' * 20)
            media = media + idade
            if sexo in 'm' and i==1:
                maisvelho=nome
                idademaior = idade
            else:
                if sexo in 'm' and idade > idademaior:
                    maisvelho=nome
                    idademaior=idade
                elif sexo in 'f' and idade <20:
                    contador = contador +1
print('a media do grupo é igual a {}'.format(media/4))
print('o nome do homem mais velho é  {}'.format(maisvelho))
print('o numero de mulheres abaixo de 20 anos é {}'.format(contador))
