print(""""
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
""")
print("\033[0;33m***\033[m"*20)
print('\033[0;31m                LOJAS BRUNÃO\033[m')
print("\033[0;33m***\033[m"*20)
compra=float(input('digite o valor da sua compra '))
print("""
digite o metodo de pagamento 
[1] - a vista dinheiro
[2] - a vista cartão
[3]- 2x no cartão
[4] -3x ou mais no cartão
""")
metpagamento=int(input('digite o metodo de pagamento: '))

if metpagamento == 1:
    desconto=(compra*10)/100
    print('sua compra de {:.2f} R$ saira com 10% de desconto no valor de {:.2f} R$'.format(compra,compra-desconto))
elif metpagamento == 2:
    desconto = (compra * 5) / 100
    print('sua compra de {:.2f} R$ saira com 5% de desconto no valor de {:.2f} R$'.format(compra,compra-desconto))
elif metpagamento == 3:
    valor = compra /2
    print('sua compra de {:.2f} R$ saira em 2x {:.2f} R$ sem juros'.format(compra,valor))
elif metpagamento == 4:
    parcelas=int(input('quantas parcelas? '))
    juros = (compra * 20) / 100
    print('sua compra de {:.2f} R$ saira com 20% de juros no valor de {:.2f} R$'.format(compra,compra+juros,))
    print('no valor de {} x {:.2f} R$'.format(parcelas,(compra+juros)/parcelas))
else:
    print('voce nao digitou uma opção valida')

