# Uma pessoa recebe R$ 1.850,00 por mês.

# Crie variáveis para armazenar:
# - Salário mensal.
salario_mensal = float(input('Qual seu salário? '))
# - Quantidade de meses trabalhados (12).
meses_trabalhado = int(input('Quantidade de meses trabalhados? '))
# - Salário anual.
salario_anual = meses_trabalhado * salario_mensal
# Calcule e exiba o salário anual.
print(f'Salário anual é: R${salario_anual:.2f}')