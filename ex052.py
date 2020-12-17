
n=int(input('digite um numero: '))

i=1
total=0

for i in range(i,n+1):
    if n % i == 0:
        print('\033[31m{}\033[m'.format(i),end=' ')
        total=total+1
    else :
        print (i,end=' ')

if total == 2:
            print('\nesse numero é PRIMO')

else:
            print('\nesse numero não é primo pois tem {} divisores'.format(total))



