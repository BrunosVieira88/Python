import math

cat1=float(input('digite o cateto oposto '))
cat2=float(input('digite o cateto adjaceste '))

#hip=math.sqrt((cat1**2)+(cat2**2))
hip=math.hypot(cat1,cat2)
print ('a hipotenusa é igual a {:.2f}'.format(hip))
