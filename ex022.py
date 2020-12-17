nome=str(input('Digite seu nome completo'))

print('seu nome em maisculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem {} letras '.format(len(nome)-nome.count(' ')))
separado = nome.split()
print('seu nome é {} e tem {} letras  '.format(separado[0],len(separado[0])))