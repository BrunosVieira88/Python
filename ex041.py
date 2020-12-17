from datetime import date
print(""""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
""")

nascimento=int(input('digite seu ano de nascimento: '))

atual=date.today().year
idade=atual-nascimento

if idade <= 9:
    print('voce tem {} e voce é MIRIM'.format(idade))
elif idade > 9 and idade <=14:
    print('voce tem {} e voce é INFANTIL'.format(idade))
elif idade > 14 and idade <=19:
    print('voce tem {} e voce é JUNIOR'.format(idade))
elif idade > 19 and idade <=25:
    print('voce tem {} e voce é SENIOR'.format(idade))
else:
    print('voce tem {} e voce é MASTER'.format(idade))