largura =float(input('digite a largura da sua parede'))
altura=float(input('digite a altura de sua parede '))

area = largura *altura
tinta =area/2

print('para pintar uma parede de {} largura por {} altura com uma area de {} m² sera necessario {} litros de tinta '.format (largura,altura,area,tinta))