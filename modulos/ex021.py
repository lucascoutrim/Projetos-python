#importei somente a função "hypot"!
from math import hypot

co = float(input('qual é o comprmento do cateto oposto?: '))
ca = float(input('qual é o comprimento do cateto adjacente?: '))

h = hypot (co, ca)

print('O comprimento da hipotenuza é de {}'.format(h))
#retorna o comprimento da hipotenuza!

