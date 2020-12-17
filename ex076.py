

print("""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.""")

print("""
    
    """)
listagem = (
            'caderno',  17.00,
            'caneta',   0.80,
            'lapis',    1.00,
            'Borracha', 0.50,
            'notepad',  1800.00)
print('*'*60)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('*'*60)

for pos in range(0, len(listagem)):
         if pos % 2 == 0 :
            print(f'{listagem[pos]:.<30}', end='')
         else:
             print(f'RS{listagem[pos]:8.2f}')
print('*'*60)