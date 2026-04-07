#soma de calorias e armazenamento das calorias digitas para calcular a média do uso diário!

calorias = []
resposta = ""

while resposta.upper() != "NÃO":
    caloria = int(input("Quantas calorias você consumiu nesta refeição?"))
    calorias.append(caloria)
    resposta = input("Você deseja informar as calorias de mais alguma refeição?")


total = 0
for caloria in calorias:
    print(f"Nesta refeição foram consumidas {calorias} calorias")
    total = total + caloria

media = total / len(calorias)
print(f"Neste dia, houve um consume médio de {media:.2f} calorias por refeição")
