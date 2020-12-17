print("""
Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
""")

zero = ('zero','um','dois','Tres','quatro','cinco','seis','sete','oito','nove','dez','onze'
        ,'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
entrada=0
saida = ''
while saida != 's':
    print('*--' * 20)
    entrada=int(input('Digite um numero de 0 a 20: '))


    if entrada >=0 and entrada <=20:

      print(f'voce digitou {zero[entrada]}')
      print('*--' * 20)
      saida=str(input('voce deseja sair [S/N]')).lower().strip()
    if saida == 's':
        break
    else:
        print('tente novamente ')
