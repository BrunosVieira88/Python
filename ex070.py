print("""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
""")
total = 0
c = 0
c2= 0
while True:
    print('*-'*20)
    produto=str(input('digite o nome do produto: '))
    valor=float(input('Digite o valor do produto R$'))
    continuar = str(input('quer continuar[S/N]')).lower().strip()

    total =total + valor
    c2 = c2+1
    if c2 ==1:
        maisbarato = produto
        mb= valor
    if mb > valor :
        maisbarato = produto

        mb = valor
    if valor > 1000:
        c= c +1
    if continuar != 's' and continuar != 'n':
        print('voce nao digitou um valor valido ')

    if continuar == 's':
        print('*-' * 20)
        print('novo cadastro')

    elif continuar == 'n':
        print('{:*^50}'.format('FIM DE JOGO'))
        break

print(f'o valor total da compra foi de R$ {total} reais.')
print(f'Forma comrados {c} produtos acima de 1.000 R$')
print(f'o produto mais barato comprado foi {maisbarato}')