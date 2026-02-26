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