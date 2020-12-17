from datetime import date
print('*---*'*10)
print ('programa que fala se um ano é bissexto')
print('apertando o 0 é usado o ano atual')
print('-----'*10)


ano=int(input('digite o ano desejado '))

if ano == 0 :
    ano= date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} NÃO é BISSEXTO'.format(ano))