import math
an =float(input('digite seu angulo '))

sen=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))

print('o seno do angulo {} é igual a {:.2f} '.format(an,sen))
print ('o coseno do angulo {} é igual a {:.2f}'.format(an,cos))
print ('a tangente do angulo {} é igual a {:.2f}'.format(an,tan))