
produto = {
    'nome':'Notebook',
    'preço':3500.00,
    'estoque':12,
    'categoria':'Informática'
}

print(produto['nome'])
print(produto['preço'])

for valor in produto.items():
    print(valor)

produto['preço'] = 3200.00
produto['fabricante'] = 'Dell'
print(produto)


