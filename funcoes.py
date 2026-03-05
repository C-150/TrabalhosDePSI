
def contar_por_atividade(atividade, participantes):
    contador = 0
    for p in participantes:
        if p[3] == atividade:
            contador += 1
    return contador

def adicionar_participante(nome, numero, idade, atividade,atividades,limite_atividade,participantes,numeros_aluno):
    if numero in numeros_aluno:
        print("Número já registado!")
        return

    if atividade not in atividades:
        print("Atividade inválida!")
        return

    if contar_por_atividade(atividade,participantes) >= limite_atividade:
        print("Esta atividade já atingiu o limite de vagas!")
        return

    participante = (nome, numero, idade, atividade)
    participantes.append(participante)
    numeros_aluno.add(numero)

    print("Participante adicionado com sucesso!")

def listar_participantes(participantes):
    if not participantes:
        print("Sem participantes.")
        return

    for p in participantes:
        print(f"Nome: {p[0]}, Nº: {p[1]}, Idade: {p[2]}, Atividade: {p[3]}")

def remover_participante(numero,participantes,numeros_aluno):
    for p in participantes:
        if p[1] == numero:
            participantes.remove(p)
            numeros_aluno.remove(numero)
            print("Participante removido!")
            return

    print("Participante não encontrado.")


def estatisticas(participantes,atividades):
    print("\n=== Estatísticas ===")
    print("Total de participantes:", len(participantes))

    if participantes:
        soma = 0
        for p in participantes:
            soma += p[2]

        media = soma / len(participantes)
        print("Média de idades:", round(media, 2))

        for atividade in atividades:
            print(f"{atividade}: {contar_por_atividade(atividade,participantes)} participantes")

def mostrar_vagas(participantes,atividades,limite_atividade):
    print("\n=== Vagas Disponíveis ===")
    for atividade in atividades:
        vagas = limite_atividade - contar_por_atividade(atividade,participantes)
        print(f"{atividade}: {vagas} vagas")

def pesquisar_participante(numero,participantes):
    for p in participantes:
        if p[1] == numero:
            print(f"Nome: {p[0]}, Nº: {p[1]}, Idade: {p[2]}, Atividade: {p[3]}")
            return
    print("Participante não encontrado.")

def atividade_mais_popular(atividades,participantes):
    maior = 0
    popular = ""

    for atividade in atividades:
        total = contar_por_atividade(atividade,participantes)
        if total > maior:
            maior = total
            popular = atividade

    if maior > 0:
        print("Atividade mais escolhida:", popular)
    else:
        print("Ainda não há participantes.")

def extremos_idade(participantes):
    if not participantes:
        print("Sem participantes.")
        return

    mais_novo = participantes[0]
    mais_velho = participantes[0]

    for p in participantes:
        if p[2] < mais_novo[2]:
            mais_novo = p
        if p[2] > mais_velho[2]:
            mais_velho = p

    print("Mais novo:", mais_novo[0], "-", mais_novo[2], "anos")
    print("Mais velho:", mais_velho[0], "-", mais_velho[2], "anos")

def listar_por_atividade(atividade,participantes):
    encontrado = False

    for p in participantes:
        if p[3] == atividade:
            print(f"Nome: {p[0]}, Nº: {p[1]}, Idade: {p[2]}")
            encontrado = True

    if not encontrado:
        print("Nenhum participante nessa atividade.")


def listar_ordenado(participantes):
    if not participantes:
        print("Sem participantes.")
        return

    lista_ordenada = sorted(participantes)

    for p in lista_ordenada:
        print(f"Nome: {p[0]}, Nº: {p[1]}, Idade: {p[2]}, Atividade: {p[3]}")

def alterar_atividade(numero, nova_atividade,participantes,atividades,limite_atividade):
    if nova_atividade not in atividades:
        print("Atividade inválida!")
        return

    if contar_por_atividade(nova_atividade,participantes) >= limite_atividade:
        print("Essa atividade já está cheia!")
        return

    for i in range(len(participantes)):
        if participantes[i][1] == numero:
            nome, num, idade, _ = participantes[i]
            participantes[i] = (nome, num, idade, nova_atividade)
            print("Atividade alterada com sucesso!")
            return

    print("Participante não encontrado.")