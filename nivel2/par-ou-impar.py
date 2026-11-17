
# Crie um programa que:
# 1. Solicite um número inteiro.
numero = int(input('Coloque um número: '))
# 2. Verifique se ele é par ou ímpar.
verificando = numero % 2
# 3. Mostre o resultado.
if verificando == 1:
    print('impar')
else:
    print('par')
