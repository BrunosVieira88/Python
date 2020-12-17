entrada =int(input('digite um numero de quatro casas decimais'))

print('unidade {:.0f}'.format(entrada/ 1 %10))
print('dezena {:.0f}'.format(entrada/10 %10))
print('centena {:.0f}'.format(entrada/100 %10))
print('milhar {:.0f}'.format(entrada/1000 %10))