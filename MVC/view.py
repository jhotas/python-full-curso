from controller import PessoaController

while True:
    decisao = int(input('(1) Salvar nova pessoa\n(2) Visualizar pessoas salvas\n(3) Sair\n'))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite seu cpf: ')

        if PessoaController.cadastrar(nome, idade, cpf):
            print('Usuário cadastrado com sucesso!')
        else:
            print('Digite os dados corretamente!')
