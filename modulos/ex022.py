#importo somente a função "radians"
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))
#Usuário vai digitar o ângulo!

rad = radians(angulo)
#transforma o algulo em radianos!

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('O valor do seno é {:.2f}!: '.format(sen))
print('O valor do cosseno é {:.2f}!: '.format(cos))
print('O valor da tangente é {:.2f}!'.format(tan))
#mostra o valor do seno, cosseno e da tangente!
