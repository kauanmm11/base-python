
vendas = ['Notebook', 'Mouse', 'Teclado', 'Mouse', 'Monitor', 'Notebook', 'Mouse']

set(vendas)
print(vendas)
conjunto = {*vendas}
print(len(conjunto))
conjunto.add('Webcam')
conjunto.remove('Monitor')
print(conjunto)
