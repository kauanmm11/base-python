
senha_cadastrado = '1234'

while True:
    senha_usuario = input('Senha do usuario: ')
    if senha_cadastrado == senha_usuario:
        print('Acesso permitido')
        break
    else:
        print('Acesso negado, Tente novamente.')

