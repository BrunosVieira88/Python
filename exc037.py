num =int(input('digite o numero a ser convertido: '))
print("""            
                   digite 1 se for binario
                   digite 2 se for octal
                   digite 3 se for hexadecimal""")
opçao=int(input('qual sua opção: '))



if opçao == 1:
    print('o numero {} em base binaria é igual a {}'.format(num,bin(num)[2:]))
elif opçao == 2:
    print('o numero {} em base binaria é igual a {}'.format(num, oct(num)[2:]))
elif  opçao == 3:
    print('o numero {} em base binaria é igual a {}'.format(num, hex(num)[2:]))

else:
    print('voce nao digitou um numero valido')