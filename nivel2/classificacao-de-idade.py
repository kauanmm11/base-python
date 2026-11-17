
# Crie um programa que solicite a idade de uma pessoa e classifique:
idade = int(input('Qual sua idade: '))
# Idade	Classificação
# 0 até 12	Criança
if idade <= 12:
    print('Criança')
# 13 até 17	Adolescente
elif idade <= 17:
    print('Adolescente')
# 18 até 59	Adulto
elif idade <= 59:
    print('Adulto')
# 60 ou mais Idoso
else:
    print('Idoso')
