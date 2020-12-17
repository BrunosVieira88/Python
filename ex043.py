print(""""
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal 
(IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
""")

peso=float(input("digite seu Peso: "))
altura=float(input("digite sua Altura: "))

imc = peso/(altura*altura)
if imc < 18.5:
    print('seu imc é {:.1f} e voce esta ABAIXO do peso'.format(imc))
elif imc > 18.5 and imc <=25:
    print('seu imc é {:.1f} e voce esta com o peso IDEAL'.format(imc))
elif imc >25 and imc <=30:
    print('seu imc é {:.1f} e voce esta com SOBREPESO'.format(imc))
elif imc >30 and imc <=40 :
    print('seu imc é {:.1f} e voce esta com OBESIDADE'.format(imc))
else:
    print('seu imc é {:.1f} e voce esta COM OBSIDADE MORBIDA VA ATE O MEDICO'.format(imc))