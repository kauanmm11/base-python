
funcionario = tuple(('nome','Kauan','idade',22,'cargo','Analista de Dados','salario',2800.00))

for tupla in funcionario:
    print(tupla)

print(funcionario[1])
print(funcionario[5])
print(len(funcionario))
funcionario = list(funcionario)
funcionario[3] = 23
funcionario = tuple(funcionario)
print(funcionario)