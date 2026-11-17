
# Crie um programa que:
# 1. Solicite três notas.
nota_pedro = float(input('Qual é a nota do pedro? '))
nota_roberto = float(input('Qual é a nota do roberto? '))
nota_carlos = float(input('Qual é a nota do carlos? '))
# 2. Calcule a média.
media_geral = (nota_pedro + nota_roberto + nota_carlos) / 3
# 3. Classifique o aluno seguindo estas regras:
# Média	Resultado
print(f'A média dos alunos é {media_geral}')
print(f'A média dos alunos é {media_geral}')
if nota_pedro >= 7:
    # 7 ou mais	Aprovado
    print('Pedro Aprovado')
elif nota_pedro >= 5:
    # Entre 5 e 6.9	Recuperação
    print('Pedro Recuperação')
else:
    # Abaixo de 5	Reprovado
    print('Pedro Reprovado')

if nota_roberto >= 7:
    # 7 ou mais	Aprovado
    print('Roberto Aprovado')
elif nota_roberto >= 5:
    # Entre 5 e 6.9	Recuperação
    print('Roberto Recuperação')
else:
    # Abaixo de 5	Reprovado
    print('Roberto Reprovado')

if nota_carlos >= 7:
    # 7 ou mais	Aprovado
    print('Carlos Aprovado')
elif nota_carlos >= 5:
    # Entre 5 e 6.9	Recuperação
    print('Carlos Recuperação')
else:
    # Abaixo de 5	Reprovado
    print('Carlos Reprovado')