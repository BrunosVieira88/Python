
print('*---*'*10)
print('Programa que le a velocidade de um veiculo e calcula multas')
print('7,00 R$ por km excedido ')
print('-----'*10)

velocidade=int(input('qual a velocidade do veiculo'))

if velocidade > 80 :
    multa=(velocidade-80)*7
    print('voce estava acima do limete de velocidade a {} km\h e recebeu uma multa de \033[7;30m{:.2f}\033[m R$'.format(velocidade,multa))

else :
    print('Continue respeitando as leis de Transito e um bom Dia')