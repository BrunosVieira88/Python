listadePalavras = ('Bruno', 'Aline', 'Wadman' , 'Isabele', 'Douglas' )



for letra in listadePalavras:
    print(f'\n{letra.upper()} nesse nome temos as vogais= ', end='')
    for vogal in letra:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}',end = " ")



