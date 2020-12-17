nota1=float(input('Digite a primeira nota'))
nota2=float(input('Digite a segunda nota'))

media=(nota1+nota2)/2

if media >=7:
    print('Voce passou de Ano! Sua nota foi {}'.format(media))
elif media >5 and media <= 5.9:
    print('voce NÃO passou tirou {} e esta de RECUPERAÇÃO!!!'.format(media))
else:
    print('voce tirou {} e esta REPROVADO'.format(media))