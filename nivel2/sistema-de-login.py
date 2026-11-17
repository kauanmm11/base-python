
# Crie um programa que:
# 1. Tenha um usuário cadastrado: kauan.
nome_usuario = input('Nome Completo: ').strip().title()
# 2. Tenha uma senha cadastrada: 12345.
senha_usuario = input('Senha: ')
# 3. Solicite usuário e senha.
nome_cadastrado = 'Kauan Medeiros Marins'
senha_cadastrado = '12345'
if nome_usuario == nome_cadastrado and senha_usuario == senha_cadastrado:
# 4. Se os dois estiverem corretos, mostre Login realizado com sucesso.
    print('Login realizado com sucesso.')
# 5. Se algum estiver errado, mostre Usuário ou senha incorretos.
else:
    print('Usuário ou senha incorretos.')
