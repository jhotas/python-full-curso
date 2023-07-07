# Defina um usuário e senha e depois verifique se
# login do usuário é válido

print('\nCADASTRO: ')
usuario = str(input('Digite um nome de usuário: '))
senha = str(input('Digite uma senha: '))

while True:
    print('\nLOGIN: ')
    login_user = str(input('Nome de usuário: '))
    senha_user = str(input('Senha: '))

    if usuario == login_user and senha == senha_user:
        print('Seja bem-vindo!')
        break
    
    print('Credenciais inválidas.')