from datetime import date
print("""" 

programa que le o ano do nascimento
ve se voce deve se ALISTAR ou NÃO

""")
nascimento=int(input('Digite o ano do seu nascimento'))

ano= date.today().year
anoalistamento=nascimento +18
idade=ano-nascimento
tempo=ano-anoalistamento

if idade > 18 :
     print('voce nasceu em {} tem {} e deveria ter se alistado em {}'.format(nascimento,idade,ano-tempo))
     print('voce deveria ter se alistado a {} anos'.format(ano-anoalistamento))

elif idade == 18:
   print ('voce tem {} e TEM QUE SE ALISTAR ESSE ANO!'.format(idade))
else:
  print('voce tem {} anos e ainda é muito novo para se alistar devera se alistar em {} '.format(idade,nascimento+18))
  print('voce devera se alistar daqui a {} anos'.format(anoalistamento-ano))