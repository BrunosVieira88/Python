print('*---*'*10)
print ('programa que calcula aumento no salario')
print('15% ate 1250 10% acima disso')
print('-----'*10)
salario=float(input('digite seu salario R$ '))

if salario > 1250:
    aumento = (salario*10)/100
    print ('seu novo salario é igual a {:.2f} R$ '.format(salario+aumento))
else:
    aumento = (salario * 15) / 100
    print('seu novo salario é igual a {:.2f} R$'.format(salario + aumento))