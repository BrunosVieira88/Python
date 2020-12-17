print('*---*'*10)
print ('programa que le se medidas podem formar triangulo')
print('-----'*10)

a=float(input('Digite o primeiro segmento '))
b=float(input('Digite o primeiro segmento '))
c=float(input('Digite o primeiro segmento '))

if a < b+c and b < c+a and c < b+a:
    print('essas medidas PODEM formar triangulo')

else:
    print('essas medidas NÃO formam triangulo')