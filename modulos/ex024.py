#importo a biblioteca random para sortear os nomes no caso!
import random

n1 = (input('Qual o nome do primeiro aluno?: '))
n2 = (input('Qual o nome do segundo aluno?: '))
n3 = (input('Qual o nome do terceiro aluno?: '))
n4 = (input('Qual o nome do quarto aluno?: '))
#Usuario vai digitar os nomes que ficaram armazenados na lista!

lista = [n1,n2,n3,n4]
#lista dos nomes digitados pelo usuário!

random.shuffle(lista)
#"random.suffle(lista) vai embaralhar os nomes da lista!

print('A ordem de apresentação vai ser {}'.format(lista))
#mostra os nomes embaralhados!
