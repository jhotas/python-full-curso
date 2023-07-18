nomes = []
def adicionar_nome(nome):
    nomes.append(nome)
    return

def pesquisa():
    pesqnome = input('Pesquise o nome:')
    nomes = list(filter(lambda nomes: nomes == pesqnome, nomes))
    print(nomes)
    return 0

def inicio():
    print('\n--- PESQUISAR PESSOAS ---')
    print('Selecione uma opção: \n1. Adicionar nome\n2. Consultar nome\n3. Encerrar')
    opcao = int(input(''))
    if opcao == 1:
        addnome = input('Digite o nome: ')
        adicionar_nome(addnome)
        print(nomes)
        return inicio()
    if opcao == 2:
        pesquisa()
        return inicio()
        
    
inicio()

#pesqnome = input('Pesquise o nome: ')
#nomes = list(filter(lambda nomes: nomes == pesqnome, nomes))
#print(nomes)