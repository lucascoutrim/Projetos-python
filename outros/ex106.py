op = 0
ficha = {}

while op !=4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informação da ficha")
    print("3 - Exibir a ficha completa ")
    print("4 - Sair")
    
    op = int(input("Informe a opção desejada: "))

    if op == 1:
        chave = input("Informe o campo que deseja  cadastral na ficha: ")
        valor = input("Infomre o dado que deseja cadastrar nesse campo: ")
        ficha.update({chave:valor})

    elif op == 2:
        print(f"Os campos disponíveis na ficha são {ficha.keys()}")
        chave = input("Informe qual campo deseja exibir: ")

        if chave in ficha.keys():
            print(f"O campo {chave} contém o dado {ficha.get(chave)}")
        else:
            print("Você digitou um campo inexistente.")

    elif op == 3:
        print("FICHA CADASTRAL")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} --> {dado}")

    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break

    else:
        print("Por favor, escolha uma opção válida")