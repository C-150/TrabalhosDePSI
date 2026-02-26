# produtos.py
# Produto: (codigo, nome, categoria, preco, stock, linguagem)
# produtos = lista de tuplos

def criar_produto(codigo, nome, categoria, preco, stock, linguagem):
    return (codigo, nome, categoria, float(preco), int(stock), linguagem)


def indice_por_codigo(produtos, codigo):
    for i in range(len(produtos)):
        if produtos[i][0] == codigo:
            return i
    return -1


def obter(produtos, codigo):
    idx = indice_por_codigo(produtos, codigo)
    if idx == -1:
        return None
    return produtos[idx]


def adicionar(produtos, produto):
    if indice_por_codigo(produtos, produto[0]) != -1:
        return False
    produtos.append(produto)
    return True


def remover(produtos, codigo):
    idx = indice_por_codigo(produtos, codigo)
    if idx == -1:
        return False
    produtos.pop(idx)
    return True


def atualizar(produtos, codigo, nome=None, categoria=None, preco=None, stock=None, linguagem=None):
    idx = indice_por_codigo(produtos, codigo)
    if idx == -1:
        return False

    c, n, cat, p, s, lang = produtos[idx]

    if nome is not None:
        n = nome
    if categoria is not None:
        cat = categoria
    if preco is not None:
        p = float(preco)
    if stock is not None:
        s = int(stock)
    if linguagem is not None:
        lang = linguagem

    produtos[idx] = (c, n, cat, p, s, lang)
    return True


def alterar_stock(produtos, codigo, delta):
    idx = indice_por_codigo(produtos, codigo)
    if idx == -1:
        return False, "Produto nao existe."

    c, n, cat, p, s, lang = produtos[idx]
    novo = s + int(delta)

    if novo < 0:
        return False, "Stock insuficiente."

    produtos[idx] = (c, n, cat, p, novo, lang)
    return True, "OK"


def formatar(produto):
    c, n, cat, p, s, lang = produto
    return f"[{c}] {n} | {cat} | {p:.2f} EUR | stock: {s} | linguagem: {lang}"


from produtos import  (
    criar_produto, adicionar, remover, obter,
    atualizar, alterar_stock, formatar
)

# Lista fixa com 30 linguagens conhecidas
LINGUAGENS = [
    "Python", "Java", "JavaScript", "C", "C++", "C#", "TypeScript", "Go", "Rust", "Kotlin",
    "Swift", "PHP", "Ruby", "R", "SQL", "Dart", "Scala", "Perl", "Haskell", "Lua",
    "Objective-C", "MATLAB", "VBA", "Julia", "Shell", "Assembly", "Visual Basic", "Elixir", "F#", "Groovy"
]


def ler_int(msg):
    while True:
        s = input(msg).strip()
        try:
            return int(s)
        except ValueError:
            print("Valor invalido.")


def ler_float(msg):
    while True:
        s = input(msg).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Valor invalido.")


def ler_texto(msg):
    return input(msg).strip()


def menu():
    print("Loja - Produtos de Programacao")
    print("1 - Listar produtos")
    print("2 - Comprar (baixar stock e calcular total)")
    print("3 - Procurar por codigo")
    print("4 - Adicionar produto (apenas linguagens da lista)")
    print("5 - Atualizar produto")
    print("6 - Remover produto")
    print("7 - Repor stock")
    print("8 - Stock baixo (<= X)")
    print("9 - Listar por linguagem")
    print("10 - Ver linguagens disponiveis")
    print("11 - Estatisticas")
    print("0 - Sair")


def mostrar_linguagens():
    print("\nLinguagens disponiveis (30):")
    for i in range(len(LINGUAGENS)):
        print(f"{i+1:02d} - {LINGUAGENS[i]}")


def escolher_linguagem():
    """
    Obriga o utilizador a escolher uma linguagem da lista.
    Permite pesquisar por texto (ex: 'ja' mostra Java e JavaScript).
    """
    while True:
        print("\nEscolha a linguagem (tem de existir na lista).")
        termo = ler_texto("Pesquisar (ENTER para ver todas): ").lower()

        if termo == "":
            candidatos = LINGUAGENS[:]
        else:
            candidatos = []
            for lang in LINGUAGENS:
                if termo in lang.lower():
                    candidatos.append(lang)

        if len(candidatos) == 0:
            print("Nao encontrei linguagens com esse termo.")
            continue

        print("\nResultados:")
        for i in range(len(candidatos)):
            print(f"{i+1} - {candidatos[i]}")

        escolha = ler_texto("Escolhe pelo numero (ou 'P' para pesquisar de novo): ").strip().upper()
        if escolha == "P":
            continue

        try:
            n = int(escolha)
            if 1 <= n <= len(candidatos):
                return candidatos[n-1]
            else:
                print("Numero fora do intervalo.")
        except ValueError:
            print("Opcao invalida.")


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nao existem produtos.")
        return
    for p in produtos:
        print(formatar(p))


def opcao_comprar(produtos):
    codigo = ler_texto("Codigo: ")
    p = obter(produtos, codigo)
    if p is None:
        print("Produto nao encontrado.")
        return

    qtd = ler_int("Quantidade: ")
    if qtd <= 0:
        print("Quantidade invalida.")
        return

    ok, msg = alterar_stock(produtos, codigo, -qtd)
    if not ok:
        print(msg)
        return

    preco_unit = p[3]
    total = preco_unit * qtd
    print("Total:", f"{total:.2f}", "EUR")
    print("Stock atual:", obter(produtos, codigo)[4])


def opcao_procurar(produtos):
    codigo = ler_texto("Codigo: ")
    p = obter(produtos, codigo)
    if p is None:
        print("Produto nao encontrado.")
    else:
        print(formatar(p))


def opcao_adicionar(produtos):
    # Nao deixa inventar linguagem: escolhe da lista
    linguagem = escolher_linguagem()

    codigo = ler_texto("Codigo: ")
    nome_base = ler_texto("Nome do produto (ex: Curso, Livro, Manual): ")
    categoria = "Programacao"
    preco = ler_float("Preco: ")
    stock = ler_int("Stock: ")

    if codigo == "" or nome_base == "":
        print("Codigo e nome sao obrigatorios.")
        return
    if preco < 0 or stock < 0:
        print("Preco e stock nao podem ser negativos.")
        return

    # Nome final amarrado a linguagem (fica coerente e nao inventa)
    nome = f"{nome_base} - {linguagem}"

    produto = criar_produto(codigo, nome, categoria, preco, stock, linguagem)

    if adicionar(produtos, produto):
        print("Produto adicionado.")
    else:
        print("Ja existe um produto com esse codigo.")


def opcao_atualizar(produtos):
    codigo = ler_texto("Codigo: ")
    p = obter(produtos, codigo)
    if p is None:
        print("Produto nao encontrado.")
        return

    print("Atual:")
    print(formatar(p))
    print("Deixar vazio para nao alterar.")

    novo_nome = ler_texto("Novo nome (sem linguagem): ")
    novo_preco_txt = ler_texto("Novo preco: ")
    novo_stock_txt = ler_texto("Novo stock: ")

    # Linguagem: opcional mudar, mas so para uma da lista
    mudar_lang = ler_texto("Mudar linguagem? (S/N): ").upper()
    linguagem = None
    if mudar_lang == "S":
        linguagem = escolher_linguagem()

    nome = None
    if novo_nome != "":
        # se mudou linguagem, usa a nova; senao usa a atual
        lang_final = linguagem if linguagem is not None else p[5]
        nome = f"{novo_nome} - {lang_final}"

    preco = None
    if novo_preco_txt != "":
        try:
            preco = float(novo_preco_txt.replace(",", "."))
            if preco < 0:
                print("Preco invalido.")
                return
        except ValueError:
            print("Preco invalido.")
            return

    stock = None
    if novo_stock_txt != "":
        try:
            stock = int(novo_stock_txt)
            if stock < 0:
                print("Stock invalido.")
                return
        except ValueError:
            print("Stock invalido.")
            return

    ok = atualizar(produtos, codigo, nome=nome, preco=preco, stock=stock, linguagem=linguagem)
    if ok:
        # se mudou linguagem mas nao mudou nome, ajusta o nome automaticamente para ficar consistente
        if linguagem is not None and nome is None:
            c, n, cat, pr, st, lang_antiga = p
            # tenta substituir " - linguagem" no fim se existir, senao apenas acrescenta
            base = n
            if " - " in n:
                base = n.split(" - ")[0]
            novo_nome_auto = f"{base} - {linguagem}"
            atualizar(produtos, codigo, nome=novo_nome_auto, linguagem=linguagem)

        print("Produto atualizado.")
        print(formatar(obter(produtos, codigo)))
    else:
        print("Nao foi possivel atualizar.")


def opcao_remover(produtos):
    codigo = ler_texto("Codigo: ")
    if remover(produtos, codigo):
        print("Produto removido.")
    else:
        print("Produto nao encontrado.")


def opcao_repor(produtos):
    codigo = ler_texto("Codigo: ")
    p = obter(produtos, codigo)
    if p is None:
        print("Produto nao encontrado.")
        return

    qtd = ler_int("Quantidade a adicionar: ")
    if qtd <= 0:
        print("Quantidade invalida.")
        return

    ok, msg = alterar_stock(produtos, codigo, qtd)
    if ok:
        print("Stock atualizado. Stock atual:", obter(produtos, codigo)[4])
    else:
        print(msg)


def opcao_stock_baixo(produtos):
    if len(produtos) == 0:
        print("Nao existem produtos.")
        return

    limite = ler_int("Limite: ")
    if limite < 0:
        print("Limite invalido.")
        return

    encontrou = False
    for p in produtos:
        if p[4] <= limite:
            print(formatar(p))
            encontrou = True

    if not encontrou:
        print("Nao existem produtos abaixo desse limite.")


def opcao_por_linguagem(produtos):
    lang = escolher_linguagem()
    encontrou = False
    for p in produtos:
        if p[5].lower() == lang.lower():
            print(formatar(p))
            encontrou = True
    if not encontrou:
        print("Nao existem produtos para essa linguagem.")


def opcao_estatisticas(produtos):
    total_prod = len(produtos)
    unidades = 0
    valor = 0.0

    for p in produtos:
        unidades += p[4]
        valor += p[3] * p[4]

    print("Numero de produtos:", total_prod)
    print("Unidades em stock:", unidades)
    print("Valor total do stock:", f"{valor:.2f}", "EUR")

    if total_prod > 0:
        mais_caro = produtos[0]
        mais_barato = produtos[0]
        for p in produtos:
            if p[3] > mais_caro[3]:
                mais_caro = p
            if p[3] < mais_barato[3]:
                mais_barato = p

        print("Mais caro:", formatar(mais_caro))
        print("Mais barato:", formatar(mais_barato))


def carregar_produtos_iniciais(produtos):
    # Produtos iniciais (todos com linguagem da lista)
    produtos.append(criar_produto("P01", "Curso Basico - Python", "Programacao", 19.99, 15, "Python"))
    produtos.append(criar_produto("P02", "Curso Completo - Java", "Programacao", 24.99, 10, "Java"))
    produtos.append(criar_produto("P03", "Livro Pratico - C", "Programacao", 17.50, 12, "C"))
    produtos.append(criar_produto("P04", "Curso Web - JavaScript", "Programacao", 21.50, 12, "JavaScript"))
    produtos.append(criar_produto("P05", "Curso Orientado a Objetos - C#", "Programacao", 26.00, 9, "C#"))
    produtos.append(criar_produto("P06", "Manual - SQL", "Programacao", 18.75, 14, "SQL"))
    produtos.append(criar_produto("P07", "Curso Sistemas - Go", "Programacao", 23.00, 8, "Go"))
    produtos.append(criar_produto("P08", "Curso Baixo Nivel - Assembly", "Programacao", 35.00, 5, "Assembly"))


def main():
    produtos = []
    carregar_produtos_iniciais(produtos)

    while True:
        menu()
        op = ler_texto("Opcao: ")

        if op == "1":
            listar_produtos(produtos)
        elif op == "2":
            opcao_comprar(produtos)
        elif op == "3":
            opcao_procurar(produtos)
        elif op == "4":
            opcao_adicionar(produtos)
        elif op == "5":
            opcao_atualizar(produtos)
        elif op == "6":
            opcao_remover(produtos)
        elif op == "7":
            opcao_repor(produtos)
        elif op == "8":
            opcao_stock_baixo(produtos)
        elif op == "9":
            opcao_por_linguagem(produtos)
        elif op == "10":
            mostrar_linguagens()
        elif op == "11":
            opcao_estatisticas(produtos)
        elif op == "0":
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()