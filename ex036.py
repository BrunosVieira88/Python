print('*---*'*10)
print ('programa que le o salario')
print('e se a parcela nao passar 30% do seu salario ele é aprovado')
print('-----'*10)

salario=float(input('digite seu salario'))
valcasa=float(input('digite o valor da casa'))
parcelas=int(input('digite anos de finaciamento'))

parcelas=parcelas*12
valorparcela=valcasa/parcelas
controle=(salario*30)/100

if valorparcela >= controle:
    print('seu emprestimo foi negado! pois vai sobrar apenas {:.2f} do seu salario de uma parcela de {:.2f} R$'.format(salario-valorparcela,valorparcela))

else:
    print('seu emprestimo foi aprovado !')
    print('voce ira pagar {:.2f} R$ em {} meses'.format(valorparcela,parcelas))