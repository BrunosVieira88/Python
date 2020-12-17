print("""
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.


""")

n=int(input('Digite um numero:'))

i=1
for i in range (i,11):
    print('{} x {} = {}'.format(n,i,n*i))