
soma = 0
contador = 5

while contador > 0:

    numero = int(input('Coloque um numero: '))
    contador -= 1
    soma += numero

    if contador == 0:
        print(f'A soma dos numero que voce colocou é {soma}')
    else:
        print('Coloque mais um numero')