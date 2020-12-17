cidade=str(input('digite a cidade que voce nasceu ')).strip()

cidade= cidade.lower()
cidade = cidade.split()

if cidade[0] == 'são' or 'sao':
    print('valido')
else:
    print('não valido')