print('*---*'*10)
print ('programa que le 3 numeros e fala qual o maior qual o menor')
print('-----'*10)
n1=int(input('digite um numero'))
n2=int(input('digite um numero'))
n3=int(input('digite um numero'))

if n1 > n2 and n1 >n3:
    print ('{} é o maior'.format(n1))
if n2>n1 and n2 > n3 :
    print('{} é o maior'.format(n2))
if n3>n1 and n3 > n2:
    print('{} é o maior'.format(n3))
if n1 < n2 and n1 <n3:
    print ('{} é o menor'.format(n1))
if n2<n1 and n2 < n3 :
    print('{} é o menor'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor'.format(n3))
