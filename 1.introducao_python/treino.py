print('--- PESQUISAR PESSOAS ---')
print('Selecione uma opção: \n1. Adicionar nome\n2. Consultar nome\n3. Encerrar')
opcao = int(input(''))

nomes = []
def adicionar_nome(nome):
    nomes.append(nome)
    return

if opcao == 1:
    addnome = input('Digite o nome: ')
    adicionar_nome(addnome)
elif opcao == 2:
    pesqnome = input('Pesquise o nome: ')
    nomes = list(filter(lambda nomes: nomes == pesqnome))
    print(nomes)