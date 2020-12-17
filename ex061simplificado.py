print("""
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
 mostrando os 10 primeiros termos da progressão usando a estrutura while.
""")
n1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão'))

primeiro = n1
contador =1

while contador <=10:
     print('{} -> '.format(primeiro), end='')
     primeiro = primeiro + r
     contador = contador +1
print('FIM')