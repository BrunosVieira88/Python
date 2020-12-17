print(""""
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes

""")
a=float(input('digite o primeiro segmento '))
b=float(input('digite o segundo segmento '))
c=float(input('digite o terceiro segmento '))

if a > b+c or b > a+b  or c > b + a :
    print('essas medidas nao formam triangulo')
elif a == b and a == c or b == c and b == a or c ==a and c == b:
    print('é um triangulo EQUILATERO')
elif a == b or a == c or b == c or b == a or c ==a or c == b:
    print('é um triangulo ISOCELES')
else:
    print('é um triangulo ESCALENO')