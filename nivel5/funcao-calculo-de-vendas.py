
def calcular_total(nome,preco,quantidade):
    preco_total = quantidade * preco
    return nome,preco_total

preco_total = calcular_total('monitor',1000,50)
print(preco_total)



def verificar_estoque(estoque):
    if estoque == 0:
        return 'Estoque esgotado'
    elif estoque <= 5:
        return 'Estoque baixo'
    else:
        return 'Estoque suficiente'
    
status_estoque = verificar_estoque(0)
print(status_estoque)



notas = [7, 8, 6, 9, 10]

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

media_alunos = calcular_media(notas)
print(media_alunos)



produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
quantidades = [5, 20, 12, 8]

def relatorio_estoque(produtos,quantidades):
    dicionario = {}
    for id in range(len(produtos)):
        produto = produtos[id]
        quantidade = quantidades[id]
        dicionario[produto] = quantidade
    return dicionario

relatorio = relatorio_estoque(produtos,quantidades)
print(relatorio)



produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
precos = [3500, 80, 120, 900]
quantidades = [2, 10, 5, 3]

def calcular_vendas(produtos,precos,quantidades):
    dicionario = {}
    for id in range(len(produtos)):
        produto =  produtos[id]
        preco = precos[id]
        quantidade = quantidades[id]
        faturamento = quantidade * preco
        dicionario[produto] = faturamento
    return dicionario

vendas = calcular_vendas(produtos,precos,quantidades)
print(vendas)


produtos = [
    {'nome': 'Arroz', 'preco': 25.50, 'quantidade': 10},
    {'nome': 'Feijão', 'preco': 8.50, 'quantidade': 20},
    {'nome': 'Macarrão', 'preco': 5.00, 'quantidade': 15}
]

def calcular_estoque(produtos):
    produto = []
    preco = []
    quantidade = []
    produtos_preco_total = {}

    for chave in produtos[0]:
        for valor in produtos:
            if chave == 'nome':
                produto.append(valor[chave])
            if chave == 'preco':
                preco.append(valor[chave])
            if chave == 'quantidade':
                quantidade.append(valor[chave])


    for i in range(len(produto)):
        produtos_preco_total[produto[i]] = quantidade[i] * preco[i]

    return produtos_preco_total

preco_total = calcular_estoque(produtos)

print(preco_total)
