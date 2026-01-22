from datetime import datetime


# ==========================================
# Mini Projeto 1 - Gerador de Siglas & Perfil
# Autor: Diogo Fernandes
# ==========================================

FICHEIRO = "perfis.txt"


def gerar_siglas(nome, signo):
    partes = nome.split()

    siglas = []

    # Sigla completa 
    sigla_completa = "".join(p[0].upper() for p in partes if p)
    siglas.append(sigla_completa)

    # Sigla curta 
    if len(partes) >= 2:
        siglas.append(partes[0][0].upper() + partes[-1][0].upper())
    else:
        siglas.append(partes[0][0].upper())

    # Nickname como sigla
    primeiro_nome = partes[0].lower()
    siglas.append(f"{primeiro_nome}_{signo.lower()}")

    return siglas


def obter_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19): return "Carneiro"
    if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20): return "Touro"
    if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20): return "Gémeos"
    if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22): return "Caranguejo"
    if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22): return "Leão"
    if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22): return "Virgem"
    if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22): return "Balança"
    if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21): return "Escorpião"
    if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21): return "Sagitário"
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19): return "Capricórnio"
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18): return "Aquário"
    return "Peixes"


def guardar_perfil(linha):
    with open(FICHEIRO, "a", encoding="utf-8") as f:
        f.write(linha + "\n")


def mostrar_perfis():
    try:
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            print("\n--- PERFIS GUARDADOS ---")
            print(f.read())
    except FileNotFoundError:
        print("Ainda não existem perfis guardados.")


# ---------------- MENU ----------------
while True:
    print("\n===== ANALISADOR DE PERFIL =====")
    print("1 - Criar perfil")
    print("2 - Ver perfis guardados")
    print("3 - Sair")
    print("--------------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o seu nome completo: ")
        data_input = input("Digite a data de nascimento (DD/MM/AAAA): ")

        try:
            data_nasc = datetime.strptime(data_input, "%d/%m/%Y")
            hoje = datetime.now()

            idade = hoje.year - data_nasc.year - (
                (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day)
            )

            signo = obter_signo(data_nasc.day, data_nasc.month)
            siglas = gerar_siglas(nome, signo)

            print("\n" + "—" * 30)
            print("RESUMO DO PERFIL")
            print(f"Nome:  {nome}")
            print(f"Idade: {idade} anos")
            print(f"Signo: {signo}")
            print("\nSIGLAS:")
            for s in siglas:
                print(f"- {s}")
            print("—" * 30)

            guardar_perfil(
                f"{nome} | {idade} | {signo} | {' / '.join(siglas)}"
            )

        except ValueError:
            print("Erro: Use o formato DD/MM/AAAA (ex: 15/05/2000)")

    elif opcao == "2":
        mostrar_perfis()

    elif opcao == "3":
        print("Programa encerrado.")
        break

