#importo a biblioteca random para sortear um nome no caso!
import random

n1 = (input('Qual o nome do primeiro aluno?: '))
n2 = (input('Qual o nome do segundo aluno?: '))
n3 = (input('Qual o nome do terceiro aluno?: '))
n4 = (input('Qual o nome do quarto aluno?: '))
#Usuario vai digitar os nomes que ficaram armazenados na lista!

lista = [n1,n2,n3,n4]

sorteado = random.choice(lista)
#o random.choice vai sortear um nome da lista!

print('O sorteado para apagar a lousa foi {}!'.format(sorteado))
#mostra o sorteado!


