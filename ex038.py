print('*---*'*10)
print ('programa que le dois numeros e diz qual é o maior')

print('-----'*10)

num1=int(input('digite um numero'))
num2=int(input('digite um numero'))


if num1 > num2:
    print(' {} é maior que {}'.format(num1,num2))
elif num2 > num1:
    print(' {} é maior que {}'.format(num2, num1))
else:
    print('os numeros sao iguais')
