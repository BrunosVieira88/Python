prod=float(input('digite o preço do produto '))

desconto= (prod * 5)/100
valor = prod-desconto

print ('o seu produto saiu de {:.2f} para {:.2f} com 5% de desconto {}'.format(prod,valor,desconto))