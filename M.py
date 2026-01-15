from datetime import datetime


# ==========================================
# Mini Projeto 1 - Gerador de Siglas & Perfil
# Autor: Diogo Fernandes
# ==========================================

def gerar_sigla(frase):
    palavras = frase.split()
    return "".join([p[0].upper() for p in palavras if len(p) > 0])


def obter_signo(dia, mes):

    # signos
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


# ---------------- MENU ----------------
while True:
    print("\n===== ANALISADOR DE PERFIL =====")
    print("1 - Gerar Sigla e Analisar Dados")
    print("2 - Sair")
    print("--------------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o seu nome completo: ")
        data_input = input("Digite a data de nascimento (DD/MM/AAAA): ")

        try:
            # Converte a string em data real
            data_nasc = datetime.strptime(data_input, "d/m/Y")
            hoje = datetime.now()

            # 1. Cálculo da Idade
            idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

            # 2. Obter Signo
            signo = obter_signo(data_nasc.day, data_nasc.month)

            # 3. Gerar Sigla
            sigla = gerar_sigla(nome)

            print("\n" + "—" * 30)
            print(f"RESUMO DO PERFIL:")
            print(f"Iniciais: {sigla}")
            print(f"Idade:    {idade} anos")
            print(f"Signo:    {signo}")
            print("—" * 30)

        except ValueError:
            print("Erro: Use o formato DD/MM/AAAA (ex: 15/05/2000)")

    elif opcao == "2":
        print("Programa encerrado.")

        break
