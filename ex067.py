print("""
Exercício Python 067: Faça um programa que mostre a tabuada de vários números
, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. 
""")
while True:
    print('-*' * 20)
    n=int(input('Digite um numero do qual deseja saber a tabuada: '))
    print('-*' * 20)

    if n < 0:
        break
    for i in range (1,11):

        print(f'{n} X {i} = {n*i}')
print('Jogo encerrado .Volte sempre!')