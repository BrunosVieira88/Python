print("""
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
""")

n1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão'))

primeiro = n1
contador =1
termos = 10
total=0
while termos != 0:
    total = total + termos
    while contador <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro = primeiro + r
        contador = contador + 1

    print('PAUSA')
    termos=int(input('quantos termos voce quer mostrar a mais: '))
print('FIM')