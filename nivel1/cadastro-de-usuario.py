# Pergunte o nome do usuário.

nome = input('Qual seu nome? ').strip().title()

# Pergunte a idade.

idade = int(input('Qual sua idade? '))

# Pergunte a altura.

altura = float(input('Qual sua altura? '))

# Mostre todas as informações na tela.

print(f'O nome do usuario é {nome}, A idade do usuario é {idade}, A altura do usuario é {altura}.')

# Mostre também o tipo de dado de cada variável usando type().

print(type(nome))
print(type(idade))
print(type(altura))
