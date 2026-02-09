disciplinas_definidas = ["Matemática", "Português", "Inglês"]
turma = []

while True:
    print("\n=====================================")
    print("          GESTOR DE TURMA")
    print("=====================================")

    print("1 - Adicionar aluno")

    if len(turma) > 0:
        print("2 - Pesquisar aluno")
        print("3 - Remover aluno")
        print("4 - Estatisticas gerais")
        print("5 - Marcar faltas")
        print("6 - Editar notas")
        print("7 - Estatisticas por disciplina")

    print("0 - Sair")
    print("-------------------------------------")

    op = input("Escolha uma opcao: ")

    if op == '1':
        nome = input("Nome do aluno: ").strip().title()
        if nome == "" or nome.isdigit():
            print("Nome invalido.")
            continue

        notas = {}
        for disciplina in disciplinas_definidas:
            while True:
                try:
                    nota = float(input(f"Nota a {disciplina} (0 a 20): "))
                    if 0 <= nota <= 20:
                        notas[disciplina] = nota
                        break
                    else:
                        print("A nota deve estar entre 0 e 20.")
                except ValueError:
                    print("Insira um numero valido.")

        while True:
            try:
                comportamento = float(input("Nota de comportamento (0 a 20): "))
                if 0 <= comportamento <= 20:
                    break
                else:
                    print("A nota deve estar entre 0 e 20.")
            except ValueError:
                print("Insira um numero valido.")

        aluno = {
            "nome": nome,
            "faltas": {"Presenca": 0, "Material": 0, "Disciplinar": 0},
            "disciplinas": notas,
            "comportamento": comportamento
        }
        turma.append(aluno)
        print("Aluno adicionado com sucesso.")

    elif op == '2' and len(turma) > 0:
        nome = input("Nome do aluno a procurar: ").title()
        for aluno in turma:
            if aluno["nome"] == nome:
                print(f"\nAluno: {aluno['nome']}")
                for tipo, valor in aluno["faltas"].items():
                    print(f"{tipo}: {valor}")
                for disciplina in disciplinas_definidas:
                    print(f"{disciplina}: {aluno['disciplinas'][disciplina]}")
                print(f"Comportamento: {aluno['comportamento']}")
                break
        else:
            print("Aluno nao encontrado.")

    elif op == '3' and len(turma) > 0:
        nome = input("Nome do aluno a remover: ").title()
        for aluno in turma:
            if aluno["nome"] == nome:
                confirmacao = input("Quer remover o aluno? (Sim ou Nao): ").lower()
                if confirmacao == "sim":
                    turma.remove(aluno)
                    print("Aluno removido.")
                break
        else:
            print("Aluno nao encontrado.")

    elif op == '4' and len(turma) > 0:
        for aluno in turma:
            soma = 0
            for disciplina in disciplinas_definidas:
                soma += aluno["disciplinas"][disciplina]
            media = soma / len(disciplinas_definidas)
            avaliacao_final = (media + aluno["comportamento"]) / 2
            print(f"{aluno['nome']} | Media: {media:.2f} | Comportamento: {aluno['comportamento']} | Avaliacao final: {avaliacao_final:.2f}")

    elif op == '5' and len(turma) > 0:
        nome = input("Nome do aluno: ").title()
        for aluno in turma:
            if aluno["nome"] == nome:
                for tipo in aluno["faltas"]:
                    while True:
                        try:
                            valor = int(input(f"Faltas de {tipo} a adicionar: "))
                            if valor >= 0:
                                aluno["faltas"][tipo] += valor
                                break
                            else:
                                print("Valor invalido, deve ser 0 ou maior.")
                        except ValueError:
                            print("Insira um numero valido.")
                print("Faltas registadas.")
                break
        else:
            print("Aluno nao encontrado.")

    elif op == '6' and len(turma) > 0:
        nome = input("Nome do aluno: ").title()
        for aluno in turma:
            if aluno["nome"] == nome:
                disc = input("Disciplina a editar: ").title()
                if disc in aluno["disciplinas"]:
                    while True:
                        try:
                            nova = float(input("Nova nota (0 a 20): "))
                            if 0 <= nova <= 20:
                                aluno["disciplinas"][disc] = nova
                                print("Nota atualizada.")
                                break
                            else:
                                print("A nota deve estar entre 0 e 20.")
                        except ValueError:
                            print("Insira um numero valido.")
                break
        else:
            print("Aluno nao encontrado.")

    elif op == '7' and len(turma) > 0:
        for disciplina in disciplinas_definidas:
            soma = 0
            maior = -1
            menor = 21
            quantidade = 0
            for aluno in turma:
                nota = aluno["disciplinas"][disciplina]
                soma += nota
                quantidade += 1
                if nota > maior:
                    maior = nota
                if nota < menor:
                    menor = nota
            media = soma / quantidade if quantidade > 0 else 0
            print(f"{disciplina} | Media: {media:.2f} | Maior nota: {maior} | Menor nota: {menor}")

    elif op == '0':
        print("Programa encerrado.")
        break

    else:
        print("Opcao invalida ou indisponivel.")
