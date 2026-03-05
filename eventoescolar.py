from funcoes import (
    adicionar_participante, remover_participante, listar_participantes,
    estatisticas, mostrar_vagas, pesquisar_participante, atividade_mais_popular,
    extremos_idade, listar_por_atividade, alterar_atividade, listar_ordenado
)

# SISTEMA DE GESTÃO - EVENTO ESCOLAR


participantes = []
numeros_aluno = set()

limite_atividade = 3
atividades = ["Teatro", "Desporto", "Música", "Artes"]

# MENU PRINCIPAL


while True:
    print("EVENTO ESCOLAR")
    print("=" * 35)
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Estatísticas")
    print("5 - Ver vagas")
    print("6 - Pesquisar")
    print("7 - Atividade mais popular")
    print("8 - Mais novo e mais velho")
    print("9 - Listar por atividade")
    print("10 - Alterar atividade")
    print("11 - Listar ordenado")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        try:
            numero = int(input("Número: "))
            idade = int(input("Idade: "))
        except ValueError:
            print("Erro! Deve introduzir números válidos.")
            continue

        print("Atividades disponíveis:", atividades)
        atividade = input("Atividade: ")
        adicionar_participante(nome, numero, idade, atividade,atividades, limite_atividade, participantes, numeros_aluno)

    elif opcao == "2":
        listar_participantes(participantes)

    elif opcao == " 0":
        print("A sair...")
        break

    elif opcao == "3":
        try:
            numero = int(input("Número do aluno a remover: "))
        except ValueError:
            print("Número inválido!")
            continue
        remover_participante(numero,participantes,numeros_aluno)

    elif opcao == "4":
        estatisticas(participantes,atividades)

    elif opcao == "5":
        mostrar_vagas(participantes,atividades,limite_atividade)

    elif opcao == "6":
        try:
            numero = int(input("Número do aluno: "))
        except ValueError:
            print("Número inválido!")
            continue
        pesquisar_participante(numero,participantes)

    elif opcao == "7":
        atividade_mais_popular(atividades,participantes)

    elif opcao == "8":
        extremos_idade(participantes)

    elif opcao == "9":
        print("Atividades disponíveis:", atividades)
        atividade = input("Qual atividade? ")
        listar_por_atividade(atividade,participantes)


    elif opcao == "10":
        try:
            numero = int(input("Número do aluno: "))
        except ValueError:
            print("Número inválido!")
            continue
        print("Atividades disponíveis:", atividades)
        nova = input("Nova atividade: ")
        alterar_atividade(numero, nova,participantes, atividades, limite_atividade)

    elif opcao == "11":
        listar_ordenado(participantes)

    else:
        print("Opção inválida!")



