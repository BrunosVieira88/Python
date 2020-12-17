maior =0
menor =0
for i in range (1,6):
         peso=float(input('digite o peso da {} pessoa '.format(i)))
         if i ==1:
             maior=peso
             menor=peso
         elif peso > maior :
             maior = peso
         elif peso < maior:
            menor = peso

print('o MAIOR peso lido foi {} kg e o MENOR foi {} kg  '.format(maior,menor))