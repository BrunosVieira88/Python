print('*---*'*10)
print ('programa que le a distancia de uma viagem')
print('e cobra 0.50 ate 200km e 0.45 mais do que isso')
print('-----'*10)


km=int(input('digite quantos km tem sua viagem '))

if km <200:

    print('o valor de sua viagem de {} km sera {:.2f} R$'.format(km,km*0.50))
else:
    print('o valor de sua viagem de {} km sera {:.2f} R$'.format(km,km*0.45))