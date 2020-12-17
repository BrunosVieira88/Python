dias=int(input('dias alugados '))
km=float(input('quantidade de Km rodados '))

diasn = dias*60
kmm = km *0.15

print('um carro alugado por {} dias e rodado {}km devera pagar {:.2f} Reais'.format(dias,km,diasn+kmm))