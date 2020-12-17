#conversor de medida

medida=float (input('coloque sua medida em metros'))

print ('{:.0f} metros em Km é igual a {} KM'.format(medida,medida/1000))
print ('{:.0f} metros em Hectometros é igual a {} Hm'.format(medida,medida/100))
print ('{:.0f} metros em Decametros é igual a {} dc'.format(medida,medida/10))
print ('{:.0f} metros em Centimetros é igual a {:.0f} cm'.format(medida,medida*100))
print ('{:.0f} metros em milimetros é igual a {:.0f} mm'.format(medida,medida*1000))