pt = int(input('digite o primeiro termo da PA '))
r = int(input('digite a razao '))

termos = 1
total=0
total2=0
contador = 10

print('{} -> '.format(pt),end='')


while contador > 1 :
 if contador == 10:
     total=pt+r
     print('{} -> '.format(total),end='')
     contador=contador-1
 else:
    total= total+r
    print('{} -> '.format(total),end='')
    contador=contador-1
print('Fim')
