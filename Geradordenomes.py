# lista onde os nomes vão ficar guardados
nomes = []

while True:
    print("\n" + "=" * 30)
    print("     GESTOR DE NOMES")
    print("=" * 30)
    print("1 - Adicionar nome")
    print("2 - Remover nome")
    print("3 - Procurar nome")
    print("4 - Editar nome")
    print("5 - Listar nomes")
    print("0 - Sair")
    print("=" * 30)

    opcao = input("Escolha uma opção: ")

    # ADICIONAR
    if opcao == "1":
        nome = input("Digite o nome a adicionar: ").strip()
        if nome == "":
            print("Nome inválido.")
        elif nome in nomes:
            print("Esse nome já existe.")
        else:
            nomes.append(nome)
            print("Nome adicionado com sucesso.")

    # REMOVER
    elif opcao == "2":
        nome = input("Digite o nome a remover: ")
        if nome in nomes:
            nomes.remove(nome)
            print("Nome removido.")
        else:
            print("Nome não encontrado.")

    # PROCURAR
    elif opcao == "3":
        nome = input("Digite o nome a procurar: ")
        if nome in nomes:
            print("Nome encontrado.")
        else:
            print("Nome não encontrado.")

    # EDITAR
    elif opcao == "4":
        nome_antigo = input("Digite o nome que deseja editar: ")
        if nome_antigo in nomes:
            nome_novo = input("Digite o novo nome: ")
            indice = nomes.index(nome_antigo)
            nomes[indice] = nome_novo
            print("Nome editado com sucesso.")
        else:
            print("Nome não encontrado.")

    # LISTAR
    elif opcao == "5":
        if nomes:
            print("Lista de nomes:")
            for i, nome in enumerate(nomes, start=1):
                print(f"{i}. {nome}")
        else:
            print("Nenhum nome cadastrado.")

    # SAIR
    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
