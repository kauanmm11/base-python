
def calcular_faturamento(preco,quantidade):
    faturamento_total = quantidade * preco
    return faturamento_total

faturamento = calcular_faturamento(1000,50)
print(faturamento)



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