nomes = []
def adicionar_nome(nome):
    nomes.append(nome)
    return

def pesquisa():
    pesqnome = input('Pesquise o nome:')
    nomes_encontrados = list(filter(lambda nome: nome == pesqnome, nomes))
    print(nomes_encontrados)
    return

def inicio():
    print('\n--- PESQUISAR PESSOAS ---')
    print('Selecione uma opção: \n1. Adicionar nome\n2. Consultar nome\n3. Encerrar')
    opcao = int(input(''))
    if opcao == 1:
        addnome = input('Digite o nome: ')
        adicionar_nome(addnome)
        print(nomes)
        return inicio()
    elif opcao == 2:
        pesquisa()
        return inicio()
    elif opcao == 3:
        print('Encerrando o programa.')
        return 0
    else: 
        print('Digite uma opção válida!')
    return inicio()
        
    
inicio()